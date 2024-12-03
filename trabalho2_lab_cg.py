import moviepy.editor as mpe #manipulação de vídeo
import numpy as np #manipulação de arrays
import matplotlib.pyplot as plt

video = mpe.VideoFileClip("Shrek.mp4")
video.ipython_display(width=480, maxduration= 200) #configurando o display do vídeo e aumentando a duração máxima

#extraindo informações
print('Tamanho:', video.size) ## ou video.h e video.w
print('FPS:', video.fps)
print('Duração:', video.duration, 'segundos')
print('Número de frames:', video.reader.nframes)

#fazendo a inversão do vídeo nos eixos

def reflexao1(frame): #eixo x
    frame_refl = np.zeros(shape=frame.shape, dtype=np.uint8)
    frame_refl[::1, ::-1] = frame

    return frame_refl

def reflexao2(frame): #eixos x e y
    frame_refl = np.zeros(shape=frame.shape, dtype=np.uint8)
    frame_refl[::-1, ::-1] = frame

    return frame_refl

def reflexao3(frame): #eixo y
    frame_refl = np.zeros(shape=frame.shape, dtype=np.uint8)
    frame_refl[::-1, ::1] = frame

    return frame_refl

def reflexao4(frame): #retorna ao normal
    frame_refl = np.zeros(shape=frame.shape, dtype=np.uint8)
    frame_refl[::1, ::1] = frame

    return frame_refl

parte1 = video.subclip(0,20)
parte2 = video.subclip(20,40).fl_image(reflexao1)
parte3 = video.subclip(40,60).fl_image(reflexao2)
parte4 = video.subclip(60,80).fl_image(reflexao3)
parte5 = video.subclip(80,100).fl_image(reflexao4)
parte6 = video.subclip(100,120).fl_image(reflexao1)
parte7 = video.subclip(120,140).fl_image(reflexao2)
parte8 = video.subclip(140,160).fl_image(reflexao3)
parte9 = video.subclip(160,180).fl_image(reflexao4)
parte10 = video.subclip(180,194.38).fl_image(reflexao1)
partes = mpe.concatenate_videoclips([parte1, parte2, parte3, parte4, parte5, parte6, parte7, parte8, parte9, parte10])

partes.ipython_display(width=480, maxduration= 200) #configurando o display do vídeo e aumentando a duração máxima

#extraindo o áudio do vídeo
a = video.audio
print('Taxa de amostragem:', a.fps, 'Hz')

#Diminuindo o áudio do vídeo
def diminuir_volume(audio, duracao_total, intervalo=30):
    segmentos = [] #lista de segmentos de vídeo
    for inicio in range(0, int(duracao_total), intervalo): #do começo ao fim do vídeo
        fim = min(inicio + intervalo, duracao_total) #definindo o fim do segmento
        fator_volume = max(0, 1 - (inicio / duracao_total)) #diminuindo o volume
        segmento = audio.subclip(inicio, fim).volumex(fator_volume) #criando o segmento
        segmentos.append(segmento) #colocando o segmento na lista
    return mpe.concatenate_audioclips(segmentos) #concatenando os segmentos e retornando o áudio

audio_diminuido = diminuir_volume(a, 194.38)
video_grave = partes.set_audio(audio_diminuido) #colocando o novo áudio no vídeo
video_grave.ipython_display(width=480, maxduration=200)

#corte e concatenação
inicio = video_grave.subclip(0,60)
corte = video_grave.subclip(60,80)
fim = video_grave.subclip(80)

video_corte = mpe.concatenate_videoclips([inicio, fim])
video_corte.ipython_display(width=480, maxduration=200)

video_final = mpe.concatenate_videoclips([video_corte, corte])
video_final.ipython_display(width=480, maxduration=200)

#salvando o resultado final
video_final.write_videofile('final.mp4')