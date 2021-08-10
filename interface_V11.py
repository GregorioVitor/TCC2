#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:55:16 2021

@author: gregorio
"""

from Bio import SeqIO
from Bio.SeqUtils import GC
import matplotlib.pyplot as plt
import sys
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.filedialog as fdlg
import tkinter.scrolledtext as tkst
from tkinter.constants import END,HORIZONTAL, VERTICAL, NW, N, E, W, S, SUNKEN, LEFT, RIGHT, TOP, BOTH, YES, NE, X, RAISED, SUNKEN, DISABLED, NORMAL, CENTER
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.lines as mlines
import os 
import pandas as pd
import numpy as np
import arff
import time
import seaborn as sns
import matplotlib.patches as mpatches
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer


lista =[]
arquivo=[]
gc_cont=[]
CheckVar1 = 0
outlier= 0
arq_f=[]


class Application:
    appname = "BioPlot"
    frameWidth  = 500
    frameHeight = 800
    
    def execute(self):
            #self.img = tk.PhotoImage(file='pascal.png')
            #self.root.iconphoto(False, self.img)
            self.root.mainloop()

    def __init__(self, master=None):
        self.root = tk.Tk()
        self.root.title(self.appname)
        self.root.geometry('%dx%d' % (self.frameWidth, self.frameHeight))
        self.fontePadrao = ("Arial", "12")
        
        self.menuInicial(None)
        
        
    def menuInicial(self, master):
        
        
        self.Container1 = Frame(master)
        self.Container1["pady"] = 10
        self.Container1.pack()
        self.titulo = Label(self.Container1, text="BioPlot")
        self.titulo["font"] = ("Arial", "18", "bold")
        self.titulo.pack()
            
            
        ###Botao###
        self.Container2 = Frame(master)
        self.Container2["padx"] = 20
        self.Container2["pady"] = 2
        self.Container2.pack()
        self.openFile = Button(self.Container2)
        self.openFile["text"] = "Open Files"
        self.openFile["font"] = ("Arial", "12")
        self.openFile["width"] = 15
        self.openFile["command"] = self.OpenFileName
        self.openFile.pack(side=LEFT)
            
        self.Remover = Button(self.Container2)
        self.Remover["text"] = "Remove All Files"
        self.Remover["font"] = ("Arial", "12")
        self.Remover["width"] = 15
        self.Remover["command"] = self.RemoveAllFiles
        self.Remover.pack(side = RIGHT)
            
        self.Remover = Button(self.Container2)
        self.Remover["text"] = "Remove Last Files"
        self.Remover["font"] = ("Arial", "12")
        self.Remover["width"] = 15
        self.Remover["command"] = self.RemoveLastOne
        self.Remover.pack(side = RIGHT)
            
            
        ###Arquivo###
        self.Container3 = Frame(master)
        self.Container3["padx"] = 20
        self.Container3["pady"] = 2
        self.Container3.pack()
        self.FileName1 = Label(self.Container3,text="", font= self.fontePadrao)
        self.FileName1.pack(side=BOTTOM) 
            
        ###Arquivo###
        self.Container4 = Frame(master)
        self.Container4["padx"] = 20
        self.Container4["pady"] = 2
        self.Container4.pack()
        self.FileName2 = Label(self.Container4,text="", font= self.fontePadrao)
        self.FileName2.pack(side=BOTTOM) 
            
        ###Arquivo###
        self.Container5 = Frame(master)
        self.Container5["padx"] = 20
        self.Container5["pady"] = 2
        self.Container5.pack()
        self.FileName3 = Label(self.Container5,text="", font= self.fontePadrao)
        self.FileName3.pack(side=BOTTOM)
            
        ###Arquivo###
        self.Container6 = Frame(master)
        self.Container6["padx"] = 20
        self.Container6["pady"] = 2
        self.Container6.pack()
        self.FileName4 = Label(self.Container6,text="", font= self.fontePadrao)
        self.FileName4.pack(side=BOTTOM) 
            
        ###Arquivo###
        self.Container7 = Frame(master)
        self.Container7["padx"] = 20
        self.Container7["pady"] = 2
        self.Container7.pack()
        self.FileName5 = Label(self.Container7,text="", font= self.fontePadrao)
        self.FileName5.pack(side=BOTTOM) 
            
        ###Arquivo###
        self.Container8 = Frame(master)
        self.Container8["padx"] = 20
        self.Container8["pady"] = 2
        self.Container8.pack()
        self.FileName6 = Label(self.Container8,text="", font= self.fontePadrao)
        self.FileName6.pack(side=BOTTOM) 
            
        ###Arquivo###
        self.Container9 = Frame(master)
        self.Container9["padx"] = 20
        self.Container9["pady"] = 2
        self.Container9.pack()
        self.FileName7 = Label(self.Container9,text="", font= self.fontePadrao)
        self.FileName7.pack(side=BOTTOM)
            
        ###Arquivo###
        self.Container10 = Frame(master)
        self.Container10["padx"] = 20
        self.Container10["pady"] = 2
        self.Container10.pack()
        self.FileName8 = Label(self.Container10,text="", font= self.fontePadrao)
        self.FileName8.pack(side=BOTTOM)
            
        ###Arquivo###
        self.Container11 = Frame(master)
        self.Container11["padx"] = 20
        self.Container11["pady"] = 2
        self.Container11.pack()
        self.FileName9 = Label(self.Container11,text="", font= self.fontePadrao)
        self.FileName9.pack(side=BOTTOM)
            
        ###Arquivo###
        self.Container12 = Frame(master)
        self.Container12["padx"] = 20
        self.Container12["pady"] = 2
        self.Container12.pack()
        self.FileName10 = Label(self.Container12,text="", font= self.fontePadrao)
        self.FileName10.pack(side=BOTTOM)
    
              
        
        
        ####Criando container extra####
        self.Container13 = Frame(master)
        self.Container13["padx"] = 20
        self.Container13["pady"] = 20
        self.Container13.pack()
        self.algo = Label(self.Container13 , text='                                         ')
        self.algo.pack(side=LEFT)
        self.Container14 = Frame(master)
        self.Container14["padx"] = 20
        self.Container14["pady"] = 20
        self.Container14.pack()
        self.algo = Label(self.Container14 , text='                                         ')
        self.algo.pack(side=LEFT)        
        self.Container15 = Frame(master)
        self.Container15["padx"] = 20
        self.Container15["pady"] = 20
        self.Container15.pack()
        self.algo = Label(self.Container15 , text='                                         ')
        self.algo.pack(side=LEFT)
        self.Container16 = Frame(master)
        self.Container16["padx"] = 20
        self.Container16["pady"] = 20
        self.Container16.pack()
        self.algo = Label(self.Container16 , text='                                         ')
        self.algo.pack(side=LEFT)
        self.Container17 = Frame(master)
        self.Container17["padx"] = 20
        self.Container17["pady"] = 20
        self.Container17.pack()
        self.algo = Label(self.Container17 , text='                                         ')
        self.algo.pack(side=LEFT)
        self.Container18 = Frame(master)
        self.Container18["padx"] = 20
        self.Container18["pady"] = 20
        self.Container18.pack()
        self.algo = Label(self.Container18 , text='                                         ')
        self.algo.pack(side=LEFT)
        
        ###Warning###
        self.ContainerWarning = Frame(master)
        self.ContainerWarning["padx"]= 20
        self.ContainerWarning["pady"]= 2
        self.ContainerWarning.pack()
        self.MessageWarning = Label(self.ContainerWarning, text="", font= ("bold", 24))
        self.MessageWarning.pack(side = BOTTOM)  
        
        ###Botao###
        self.BotaoNextBack = Frame(master)
        self.BotaoNextBack["padx"] = 20
        self.BotaoNextBack["pady"] = 20
        self.BotaoNextBack.pack()        
        self.Next = Button(self.BotaoNextBack)
        self.Next["text"] = "Next"
        self.Next["font"] = ("Arial", "12")
        self.Next["width"] = 15
        self.Next["command"] = lambda:self.menuFeatures(None)
        self.Next.pack(side = RIGHT)
        
        
        i=0
        if(lista):
            while(i < len(lista)):
                if(i==0):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName1["text"] = lista[i]
                    i=i+1
                elif(i==1):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName2["text"] = lista[i]
                    i=i+1
                elif(i==2):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName3["text"] = lista[i]
                    i=i+1
                elif(i==3):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName4["text"] = lista[i]
                    i=i+1
                elif(i==4):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName5["text"] = lista[i]
                    i=i+1
                elif(i==5):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName6["text"] = lista[i]
                    i=i+1
                elif(i==6):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName7["text"] = lista[i]
                    i=i+1
                elif(i==7):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName8["text"] = lista[i]
                    i=i+1
                elif(i==8):
                    self.MessageWarning["text"] = "File add"
                    self.MessageWarning["fg"] = "black"
                    self.FileName9["text"] = lista[i]
                    i=i+1
                elif(i==9):
                    self.FileName10["text"] = lista[i]
                    self.MessageWarning["text"] = "File add, can't add more files"
                    self.MessageWarning["fg"] = "black"
                    i=i+1
                self.root.update()    
        
        
#Função para apagar tudo o que estava na interface        
    def apagaBotoes(self, master):

        self.Container1.pack_forget()
        self.Container2.pack_forget()
        self.Container3.pack_forget()
        self.Container4.pack_forget()
        self.Container5.pack_forget()
        self.Container6.pack_forget()
        self.Container7.pack_forget()
        self.Container8.pack_forget()
        self.Container9.pack_forget()
        self.Container10.pack_forget()
        self.Container11.pack_forget()
        self.Container12.pack_forget()
        self.Container13.pack_forget()
        self.Container14.pack_forget()
        self.Container15.pack_forget()
        self.Container16.pack_forget()
        self.Container17.pack_forget()
        self.Container18.pack_forget()
        self.ContainerWarning.pack_forget()
        self.BotaoNextBack.pack_forget()
        
        
#função para apagar tudo e voltar para tela inicial        
    def voltarTelaInicial(self, master):
        self.apagaBotoes(None)
        self.menuInicial(None)
        
        
        
#Função para criar um menu com as features        
    def menuFeatures(self, master):
        
        if(lista):
            self.apagaBotoes(None)
            
            self.Container1 = Frame(master)
            self.Container1["pady"] = 10
            self.Container1.pack()
            self.titulo = Label(self.Container1, text="BioPlot")
            self.titulo["font"] = ("Arial", "18", "bold")
            self.titulo.pack()
            
            
            ###Label Frame 1###
            self.Container2 = LabelFrame(master, text = "BoxPlot")
            self.Container2["padx"] = 20
            self.Container2["pady"] = 10
            self.Container2.pack()
            
            ###spinbox###
            self.Container3 = Label(self.Container2)
            self.Container3["padx"] = 2
            self.Container3["pady"] = 2
            self.Container3.pack()
            self.BDnumber = Spinbox(self.Container3, values = (1,2,3,4, 5, 6, 7, 8, 9, 10), width = 2)
            self.BDnumber.pack(side= RIGHT)
            self.textoBDnumber = Label(self.Container3, text="Number of BD's")
            self.textoBDnumber["font"] = ("Arial", "10")
            self.textoBDnumber.pack(side = RIGHT)
            
            ###CheckBox###
            self.CheckVar1 =IntVar()         
            self.C1 = Checkbutton(self.Container2, text = " Show Outliers", variable = self.CheckVar1, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 20)
            self.C1.pack()
                
            ###Spinbox###
            self.Container4 = Label(self.Container2)
            self.Container4["padx"] = 2
            self.Container4["pady"] = 5
            self.Container4.pack()
            self.FontSize = Spinbox(self.Container4, values = (6, 8, 10, 12, 14, 16, 18, 20), width = 2)
            self.FontSize.pack(side= RIGHT)
            self.textoFontSize = Label(self.Container4, text="Font Size")
            self.textoFontSize["font"] = ("Arial", "10")
            self.textoFontSize.pack(side = RIGHT)
            
            ###Botao###
            self.Width = Button(self.Container2)
            self.Width["text"] = "Width"
            self.Width["font"] = ("Arial", "12")
            self.Width["width"] = 12
            self.Width["command"] = self.width
            self.Width.pack(side = LEFT)
                
            ###Botao###
            self.GcContent = Button(self.Container2)
            self.GcContent["text"] = "GC Content"
            self.GcContent["font"] = ("Arial", "12")
            self.GcContent["width"] = 12
            self.GcContent["command"] = self.GContent
            self.GcContent.pack(side = LEFT)
                
            ###Botao###
            self.GcRatio = Button(self.Container2)
            self.GcRatio["text"] = "GC Ratio"
            self.GcRatio["font"] = ("Arial", "12")
            self.GcRatio["width"] = 12
            self.GcRatio["command"] = self.Ratio
            self.GcRatio.pack(side = LEFT)
               
            ###Espaço entre os Label Frames####
            self.Container5 = Frame(master)
            self.Container5["padx"] = 82
            self.Container5["pady"] = 2
            self.Container5.pack()
            self.algo = Label(self.Container5, text='                                         ')
            self.algo.pack(side=LEFT)
            
            
            
            ###Label Frame 2###
            self.Container4 = LabelFrame(master, text = "BarPlot")
            self.Container4["padx"] = 82
            self.Container4["pady"] = 10
            self.Container4.pack()
            
            
            ###Botao###
            self.Dinuc = Button(self.Container4)
            self.Dinuc["text"] = "Dinucleotide"
            self.Dinuc["font"] = ("Arial", "12")
            self.Dinuc["width"] = 12
            self.Dinuc["command"] = self.Dinucleotide
            self.Dinuc.pack(side = LEFT)
            
            ###Botao###
            self.Trinuc = Button(self.Container4)
            self.Trinuc["text"] = "Trinucleotide"
            self.Trinuc["font"] = ("Arial", "12")
            self.Trinuc["width"] = 12
            self.Trinuc["command"] = self.Trinucleotide
            self.Trinuc.pack(side = RIGHT)
            
            ###Espaço entre os Label Frames####
            self.Container12 = Frame(master)
            self.Container12["padx"] = 82
            self.Container12["pady"] = 2
            self.Container12.pack()
            self.algo = Label(self.Container12, text='                                         ')
            self.algo.pack(side=LEFT)
            
                
            
            ###Label Frame 3###
            self.Container6 = LabelFrame(master, text = "Save in text")
            self.Container6["padx"] = 82
            self.Container6["pady"] = 10
            self.Container6.pack()
            
            ###Botao###
            self.SaveDF = Button(self.Container6)
            self.SaveDF["text"] = "Save in CSV"
            self.SaveDF["font"] = ("Arial", "12")
            self.SaveDF["width"] = 12
            self.SaveDF["command"] = self.SaveCsv
            self.SaveDF.pack(side = LEFT)
            
            ###Botao###
            self.SaveARFF = Button(self.Container6)
            self.SaveARFF["text"] = "Save in ARFF"
            self.SaveARFF["font"] = ("Arial", "12")
            self.SaveARFF["width"] = 12
            self.SaveARFF["command"] = self.ARFF
            self.SaveARFF.pack(side = RIGHT)
            
            ###Espaço entre os Label Frames####
            self.Container13 = Frame(master)
            self.Container13["padx"] = 82
            self.Container13["pady"] = 2
            self.Container13.pack()
            self.algo = Label(self.Container13, text='                                         ')
            self.algo.pack(side=LEFT)
            
                
            
            ###Label Frame 4###
            self.Container7 = LabelFrame(master, text = "Autocorrelation")
            self.Container7["padx"] = 32
            self.Container7["pady"] = 10
            self.Container7.pack()
            
            ###Label Frame dentro do Label Frame###
            self.Container8 = LabelFrame(self.Container7, text="Dinucleotide")
            self.Container8["padx"] = 48
            self.Container8["pady"] = 10
            self.Container8.pack()
            
            self.Container9 = Label(self.Container8)
            self.Container9["padx"] = 2
            self.Container9["pady"] = 10
            self.Container9.pack()
            #self.PhysicalStructuresDi = Spinbox(self.Container9, values = ('twist', 'tilt', 'roll', 'shift', 'slide', 'rise'), width = 5)
            #self.PhysicalStructuresDi.pack(side= RIGHT)
            #self.textoPhysicalStructuresDi = Label(self.Container9, text="Physical Structures")
            #self.textoPhysicalStructuresDi["font"] = ("Arial", "10")
            #self.textoPhysicalStructuresDi.pack(side = RIGHT)
            
            self.Container14 = Label(self.Container9)
            self.Container14["padx"] = 2
            self.Container14["pady"] = 10
            self.Container14.pack()
            
            ###CheckBox###
            self.CheckVar2 =IntVar()         
            self.C2 = Checkbutton(self.Container14, text = "Twist", variable = self.CheckVar2, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 5)
            self.C2.pack(side = LEFT)
            
            ###CheckBox###
            self.CheckVar3 =IntVar()         
            self.C3 = Checkbutton(self.Container14, text = "Tilt", variable = self.CheckVar3, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 5)
            self.C3.pack(side = LEFT)
            
            ###CheckBox###
            self.CheckVar4 =IntVar()         
            self.C4 = Checkbutton(self.Container14, text = "Roll", variable = self.CheckVar4, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 5)
            self.C4.pack(side = LEFT)
            
            self.Container15 = Label(self.Container9)
            self.Container15["padx"] = 2
            self.Container15["pady"] = 10
            self.Container15.pack()
            
            self.CheckVar5 =IntVar()         
            self.C5 = Checkbutton(self.Container15, text = "Shift", variable = self.CheckVar5, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 5)
            self.C5.pack(side = LEFT)
            
            self.CheckVar6 =IntVar()         
            self.C6 = Checkbutton(self.Container15, text = "Slide", variable = self.CheckVar6, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 5)
            self.C6.pack(side = LEFT)
            
            self.CheckVar7 =IntVar()         
            self.C7 = Checkbutton(self.Container15, text = "Rise", variable = self.CheckVar7, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 5)
            self.C7.pack(side = LEFT)
            
            
            self.Container17 = Label(self.Container9)
            self.Container17["padx"] = 2
            self.Container17["pady"] = 5
            self.Container17.pack()
            self.LagDi = Spinbox(self.Container17, values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), width = 2)
            self.LagDi.pack(side= RIGHT)
            self.textLagDi = Label(self.Container17, text="LAG")
            self.textLagDi["font"] = ("Arial", "10")
            self.textLagDi.pack(side = RIGHT)
            
            ###Botao###
            self.SaveDAC = Button(self.Container8)
            self.SaveDAC["text"] = "DAC"
            self.SaveDAC["font"] = ("Arial", "12")
            self.SaveDAC["width"] = 12
            self.SaveDAC["command"] = self.DAC
            self.SaveDAC.pack(side = LEFT)
            
            ###Botao###
            self.SaveDCC = Button(self.Container8)
            self.SaveDCC["text"] = "DCC"
            self.SaveDCC["font"] = ("Arial", "12")
            self.SaveDCC["width"] = 12
            self.SaveDCC["command"] = self.DCC
            self.SaveDCC.pack(side = LEFT)
            
            
            
            ###Label Frame dentro do Label Frame###
            self.Container10 = LabelFrame(self.Container7, text="Trinucleotide")
            self.Container10["padx"] = 48
            self.Container10["pady"] = 10
            self.Container10.pack()
            
            self.Container11 = Label(self.Container10)
            self.Container11["padx"] = 2
            self.Container11["pady"] = 10
            self.Container11.pack()
            #self.PhysicalStructuresTri = Spinbox(self.Container11, values = ('Bendability(DNAse)', 'Dnase I'), width = 18)
            #self.PhysicalStructuresTri.pack(side= RIGHT)
            #self.textoPhysicalStructuresTri = Label(self.Container11, text="Physical Structures")
            #self.textoPhysicalStructuresTri["font"] = ("Arial", "10")
            #self.textoPhysicalStructuresTri.pack(side = RIGHT)
            
            self.Container16 = Label(self.Container11)
            self.Container16["padx"] = 2
            self.Container16["pady"] = 10
            self.Container16.pack()
            
            
            self.CheckVar8 =IntVar()         
            self.C8 = Checkbutton(self.Container16, text = "Bendability(DNAse)", variable = self.CheckVar8, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 18)
            self.C8.pack(side = LEFT)
            
            self.CheckVar9 =IntVar()         
            self.C9 = Checkbutton(self.Container16, text = "Dnase I", variable = self.CheckVar9, \
                     onvalue = 1, offvalue = 0, height=2, \
                     width = 7)
            self.C9.pack(side = LEFT)
            
            self.Container18 = Label(self.Container11)
            self.Container18["padx"] = 2
            self.Container18["pady"] = 5
            self.Container18.pack()
            self.LagTri = Spinbox(self.Container18, values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), width = 2)
            self.LagTri.pack(side= RIGHT)
            self.textLagTri = Label(self.Container18, text="LAG")
            self.textLagTri["font"] = ("Arial", "10")
            self.textLagTri.pack(side = RIGHT)
            
            ###Botao###
            self.SaveTAC = Button(self.Container10)
            self.SaveTAC["text"] = "TAC"
            self.SaveTAC["font"] = ("Arial", "12")
            self.SaveTAC["width"] = 12
            self.SaveTAC["command"] = self.TAC
            self.SaveTAC.pack(side = LEFT)
            
            ###Botao###
            self.SaveTCC = Button(self.Container10)
            self.SaveTCC["text"] = "TCC"
            self.SaveTCC["font"] = ("Arial", "12")
            self.SaveTCC["width"] = 12
            self.SaveTCC["command"] = self.TCC
            self.SaveTCC.pack(side = LEFT)
            
            
            ###Warning###
            self.ContainerWarning = Frame(master)
            self.ContainerWarning["padx"]= 20
            self.ContainerWarning["pady"]= 2
            self.ContainerWarning.pack()
            self.MessageWarning = Label(self.ContainerWarning, text="", font= ("bold", 24))
            self.MessageWarning.pack(side = BOTTOM)  
            
            
            ###Botao###
            self.BotaoNextBack = Frame(master)
            self.BotaoNextBack["padx"] = 20
            self.BotaoNextBack["pady"] = 20
            self.BotaoNextBack.pack()
            self.Back = Button(self.BotaoNextBack)
            self.Back["text"] = "Back"
            self.Back["font"] = ("Arial", "12")
            self.Back["width"] = 12
            self.Back["command"] = lambda:self.voltarTelaInicial(None)
            self.Back.pack(side = LEFT)
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()
        
        
          
        
        
    def OpenFileName(self):
        self.MessageWarning["text"] = ""
        self.MessageWarning["fg"] = "black"
        self.root.update()
        
        opcoes = {}
        opcoes['defaultextension'] = '.fasta'
        opcoes['filetypes'] = [('Arquivos fasta', '.fasta .fa '),('Arquivos texto', '.txt'), ('Todos os arquivos', '.*')]
        opcoes['initialdir'] = ''
        opcoes['initialfile'] = ''
        #opcoes['parent'] = self.root
        opcoes['title'] = 'Open File'
        
        
        nomeArquivo = fdlg.askopenfilename(**opcoes)
        ArquivoBasename = os.path.basename(nomeArquivo)
        
        
        if(nomeArquivo):
            if(len(lista) < 10):
                lista.append(str(nomeArquivo))
                arq_f.append(ArquivoBasename.rstrip('.fasta').replace('_', " ")) ##colocando o nome dos database em vetor sem o .fasta
                
            if(len(lista)==1):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName1["text"] = lista[0]
            elif(len(lista)==2):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName2["text"] = lista[1]
            elif(len(lista)==3):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName3["text"] = lista[2]
            elif(len(lista)==4):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName4["text"] = lista[3]
            elif(len(lista)==5):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName5["text"] = lista[4]
            elif(len(lista)==6):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName6["text"] = lista[5]
            elif(len(lista)==7):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName7["text"] = lista[6]
            elif(len(lista)==8):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName8["text"] = lista[7]
            elif(len(lista)==9):
                self.MessageWarning["text"] = "File add"
                self.MessageWarning["fg"] = "black"
                self.FileName9["text"] = lista[8]
            elif(len(lista)==10):
                self.FileName10["text"] = lista[9]
                self.MessageWarning["text"] = "File add, can't add more files"
                self.MessageWarning["fg"] = "black"
            self.root.update()    
     
        
    def RemoveAllFiles(self):
        self.MessageWarning["text"] = ""
        self.MessageWarning["fg"] = "black"
        self.root.update()
        
        if(len(lista) > 0):
            msgBox = messagebox.askyesno("Remove all files", "Do you want to remove all files?")
            if msgBox == True:
                lista.clear()
                arq_f.clear()
                
                self.FileName1["text"] = ""
                self.FileName2["text"] = ""
                self.FileName3["text"] = ""
                self.FileName4["text"] = ""
                self.FileName5["text"] = ""
                self.FileName6["text"] = ""
                self.FileName7["text"] = ""
                self.FileName8["text"] = ""
                self.FileName9["text"] = ""
                self.FileName10["text"] = ""
                self.MessageWarning["text"] = "All files removed"
                self.MessageWarning["fg"] = "black"
                self.root.update()
        else:
            self.MessageWarning["text"] = "No files to remove"
            self.MessageWarning["fg"] = "red"
            self.root.update()
        

    def RemoveLastOne(self):
        self.MessageWarning["text"] = ""
        self.MessageWarning["fg"] = "black"
        self.root.update()
        
        var = len(lista)
        if(var >0):
            msgBox = messagebox.askyesno("Remove last file", "Do you want to remove the last file?")
            if msgBox == True:
                lista.pop()
                arq_f.pop()
                self.MessageWarning["text"] = "File removed"
                self.MessageWarning["fg"] = "black"
                self.root.update()
                if(var== 1):
                    self.FileName1["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 2):
                    self.FileName2["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 3):
                    self.FileName3["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 4):
                    self.FileName4["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 5):
                    self.FileName5["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 6):
                    self.FileName6["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 7):
                    self.FileName7["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 8):
                    self.FileName8["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 9):
                    self.FileName9["text"] = ""
                    self.MessageWarning["fg"] = "black"
                elif(var== 10):
                    self.FileName10["text"] = ""
                    self.MessageWarning["fg"] = "black"
                self.root.update()
        else:
            self.MessageWarning["text"] = "No files to remove"
            self.MessageWarning["fg"] = "red"
            self.root.update()
        
    
    def criarBoxplot(self, arquivo_plot):
            if(self.CheckVar1.get()==1):
                outlier = True
            else:
                outlier = False
                
            leg_diamond = mlines.Line2D([], [], marker='D',lw=0, label='Mean', color = 'red')
            line = mlines.Line2D([],[], lw=1.5, label= 'Median', color='black')
            
            
            
            if self.BDnumber.get()== "1":
                blue_patch = mpatches.Patch(color='dodgerblue', label='The blue data')
                diamond = dict(markerfacecolor='red', marker='D')
                sns.boxplot(data = arquivo_plot, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, color="dodgerblue", medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})
                plt.legend([blue_patch, leg_diamond, line], ['Database1', 'Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            elif self.BDnumber.get()== "2":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, leg_diamond, line], ['Database1', 'Database2','Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            elif self.BDnumber.get()== "3":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                yellow_patch = mpatches.Patch(color='yellow', label='The yellow data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green", "yellow"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, yellow_patch, leg_diamond, line], ['Database1', 'Database2', 'Database3','Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
                
            elif self.BDnumber.get()== "4":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                yellow_patch = mpatches.Patch(color='yellow', label='The yellow data')
                orange_patch = mpatches.Patch(color='orange', label='The orange data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green", "yellow", "orange"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, yellow_patch, orange_patch, leg_diamond, line], ['Database1', 'Database2', 'Database3', 'Database4', 'Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            elif self.BDnumber.get()== "5":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                yellow_patch = mpatches.Patch(color='yellow', label='The yellow data')
                orange_patch = mpatches.Patch(color='orange', label='The orange data')
                purple_patch = mpatches.Patch(color='purple', label='The purple data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green", "yellow", "orange", "purple"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, yellow_patch, orange_patch, purple_patch, leg_diamond, line], ['Database1', 'Database2', 'Database3', 'Database4', 'Database5', 'Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            elif self.BDnumber.get()== "6":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                yellow_patch = mpatches.Patch(color='yellow', label='The yellow data')
                orange_patch = mpatches.Patch(color='orange', label='The orange data')
                purple_patch = mpatches.Patch(color='purple', label='The purple data')
                brown_patch = mpatches.Patch(color='saddlebrown', label='The brown data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green", "yellow", "orange", "purple", "saddlebrown"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, yellow_patch, orange_patch, purple_patch, brown_patch,leg_diamond, line], ['Database1', 'Database2', 'Database3', 'Database4', 'Database5', 'Database6', 'Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            elif self.BDnumber.get()== "7":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                yellow_patch = mpatches.Patch(color='yellow', label='The yellow data')
                orange_patch = mpatches.Patch(color='orange', label='The orange data')
                purple_patch = mpatches.Patch(color='purple', label='The purple data')
                brown_patch = mpatches.Patch(color='saddlebrown', label='The brown data')
                pink_patch = mpatches.Patch(color='pink', label='The pink data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green", "yellow", "orange", "purple", "saddlebrown", "pink"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, yellow_patch, orange_patch, purple_patch, brown_patch, pink_patch,leg_diamond, line], ['Database1', 'Database2', 'Database3', 'Database4', 'Database5', 'Database6', 'Database7', 'Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            elif self.BDnumber.get()== "8":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                yellow_patch = mpatches.Patch(color='yellow', label='The yellow data')
                orange_patch = mpatches.Patch(color='orange', label='The orange data')
                purple_patch = mpatches.Patch(color='purple', label='The purple data')
                brown_patch = mpatches.Patch(color='saddlebrown', label='The brown data')
                pink_patch = mpatches.Patch(color='pink', label='The pink data')
                gray_patch = mpatches.Patch(color='gray', label='The gray data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green", "yellow", "orange", "purple", "saddlebrown", "pink", "gray"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, yellow_patch, orange_patch, purple_patch, brown_patch, pink_patch, gray_patch, leg_diamond, line], ['Database1', 'Database2', 'Database3', 'Database4', 'Database5', 'Database6', 'Database7', 'Database8', 'Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            elif self.BDnumber.get()== "9":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                yellow_patch = mpatches.Patch(color='yellow', label='The yellow data')
                orange_patch = mpatches.Patch(color='orange', label='The orange data')
                purple_patch = mpatches.Patch(color='purple', label='The purple data')
                brown_patch = mpatches.Patch(color='saddlebrown', label='The brown data')
                pink_patch = mpatches.Patch(color='pink', label='The pink data')
                gray_patch = mpatches.Patch(color='gray', label='The gray data')
                cyan_patch = mpatches.Patch(color='cyan', label='The cyan data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green", "yellow", "orange", "purple", "saddlebrown", "pink", "gray", "cyan"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, yellow_patch, orange_patch, purple_patch, brown_patch, pink_patch, gray_patch, cyan_patch,leg_diamond, line], ['Database1', 'Database2', 'Database3', 'Database4', 'Database5', 'Database6', 'Database7', 'Database8','Database9', 'Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            elif self.BDnumber.get()== "10":
                blue_patch = mpatches.Patch(color='blue', label='The blue data')
                green_patch = mpatches.Patch(color='green', label='The green data')
                yellow_patch = mpatches.Patch(color='yellow', label='The yellow data')
                orange_patch = mpatches.Patch(color='orange', label='The orange data')
                purple_patch = mpatches.Patch(color='purple', label='The purple data')
                brown_patch = mpatches.Patch(color='saddlebrown', label='The brown data')
                pink_patch = mpatches.Patch(color='pink', label='The pink data')
                gray_patch = mpatches.Patch(color='gray', label='The gray data')
                cyan_patch = mpatches.Patch(color='cyan', label='The cyan data')
                olive_patch = mpatches.Patch(color='olive', label='The olive data')
                diamond = dict(markerfacecolor='red', marker='D')
                my_color = ["dodgerblue" ,"green", "yellow", "orange", "purple", "saddlebrown", "pink", "gray", "cyan", "olive"]
                sns.boxplot(data = arquivo_plot, palette= my_color, showfliers=outlier, linewidth=1.5, saturation=1, showmeans=True, meanprops=diamond, width=0.3, medianprops={'color':'black'}, boxprops={'edgecolor': 'black'}, capprops={'color': 'black'})   
                plt.legend([blue_patch, green_patch, yellow_patch, orange_patch, purple_patch, brown_patch, pink_patch, gray_patch, cyan_patch, olive_patch,leg_diamond, line], ['Database1', 'Database2', 'Database3', 'Database4', 'Database5', 'Database6', 'Database7', 'Database8','Database9', 'Database10', 'Mean', 'Median'], frameon=True, fontsize=14).get_frame().set_edgecolor('b')
            
            ##nomeando cada boxplot##
            plt.xticks(range(len(arq_f)), arq_f)
            plt.tick_params(axis='x', which='major', labelsize=self.FontSize.get())
        
    
    def width(self):
        if lista:
            self.MessageWarning["text"] = "Loading"
            self.MessageWarning["fg"] = "black"
            self.root.update()
            arquivo = []
            
            for aux in range(0, len(lista)):
                arquivo.append([len(rec) for rec in SeqIO.parse(lista[aux],"fasta")]) ##salvando o comprimento de cada sequencia de cada database em vetor
        
            for aux in range(0, len(lista)):
                name=[]
                width=[]
                data=[]
                for rec in SeqIO.parse(lista[aux],"fasta"):
                    name.append(rec.id)
                    width.append(len(rec))
                data = np.array([name, width]).T
                df = pd.DataFrame(data, columns = ['Seq Name','Width'])
                    
                file = open('Results/Features/Width of '+ arq_f[aux] + '.csv', 'w')
                df.to_csv(r'Results/Features/Width of '+ arq_f[aux] + '.csv', index = True)
                file.close()      
        
            plt.style.use(['seaborn-whitegrid']) 
            plt.figure(figsize=(24,12))
            fonte = {'weight':'bold', 'size': 26}
            plt.xlabel("Databases", fontdict=fonte)
            plt.ylabel("Sequence Length", fontdict=fonte)
            plt.title("Sequence Length", fontdict=fonte)
            plt.autoscale()
            plt.yticks(np.arange(0,100000, step=300))
            
            self.criarBoxplot(arquivo)
                        
            if(self.CheckVar1.get()==1):
                plt.savefig("Results/Plots/BoxPlotWidth_WithOL.png")
            else:
                plt.savefig("Results/Plots/BoxPlotWidth.png")
            
            self.MessageWarning["text"] = "Width plotted"
            self.MessageWarning["fg"] = "black"
            self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()
        

    def GContent(self):
        if lista:
            self.MessageWarning["text"] = "Loading"
            self.MessageWarning["fg"] = "black"
            self.root.update()
            
            gc_cont = []
            for aux in range(0, len(lista)):
                gc_cont.append([GC(rec.seq) for rec in SeqIO.parse(lista[aux],"fasta")]) 
            
            for aux in range(0, len(lista)):
                name=[]
                gc=[]
                data=[]
                for rec in SeqIO.parse(lista[aux],"fasta"):
                    name.append(rec.id)
                    gc.append(GC(rec.seq))
                data = np.array([name, gc]).T
                df = pd.DataFrame(data, columns = ['Seq Name','GC Content'])
                    
                file = open('Results/Features/GC Content of '+ arq_f[aux] + '.csv', 'w')
                df.to_csv(r'Results/Features/GC Content of '+ arq_f[aux] + '.csv', index = True)
                file.close()
            
            plt.style.use(['seaborn-whitegrid'])
            plt.figure(figsize=(24,12))
            fonte = {'weight':'bold', 'size': 26}
            plt.xlabel("Databases", fontdict=fonte)
            plt.ylabel("GC%", fontdict=fonte)
            plt.title("GC Content", fontdict=fonte)
            plt.autoscale()
            
            
            
            self.criarBoxplot(gc_cont)
            
            if(self.CheckVar1.get()==1):
                plt.savefig("Results/Plots/BoxPlotContent_withOL.png")
            else:    
                plt.savefig("Results/Plots/BoxPlotContent.png")
            
            self.MessageWarning["text"] = "GC Content plotted"
            self.MessageWarning["fg"] = "black"
            self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()


    def Ratio(self):
        if lista:
            self.MessageWarning["text"] = "Loading"
            self.MessageWarning["fg"] = "black"
            self.root.update()
            
            nucleotideos =['A','C','G','T']
            GC_ratio_list = []
            con_nuc=[]
            for aux in range(0, len(lista)):
                data=[]
                name=[]
                for rec in SeqIO.parse(lista[aux],"fasta"):
                    seq_nuc = rec.seq    
                    all_counts = [] #quantidade de nucleotideo de cada sequencia
                    for nucleotide in nucleotideos:
                        count = seq_nuc.count(nucleotide)
                        all_counts.append(count)
                    if (all_counts[1]) > 0:    
                        GC_ratio_list.append((all_counts[2])/(all_counts[1]))
                        name.append(rec.id)
                data = np.array([name, GC_ratio_list]).T
                df = pd.DataFrame(data, columns = ['Seq Name','GC Ratio'])
                    
                file = open('Results/Features/GC Ratio of '+ arq_f[aux] + '.csv', 'w')
                df.to_csv(r'Results/Features/GC Ratio of '+ arq_f[aux] + '.csv', index = True)
                file.close()
                
                con_nuc.append(GC_ratio_list)
                GC_ratio_list = [] 
                
                
            
            
            plt.style.use(['seaborn-whitegrid'])
            plt.figure(figsize=(24,12))
            fonte = {'weight':'bold', 'size': 26}
            plt.xlabel("Databases", fontdict=fonte)
            plt.ylabel("Ratio", fontdict=fonte)
            plt.title("GC Ratio", fontdict=fonte)
            plt.autoscale()
            
            self.criarBoxplot(con_nuc)
            
            if(self.CheckVar1.get()==1):
                plt.savefig("Results/Plots/BoxPlotRatio_withOL.png")
            else:
                plt.savefig("Results/Plots/BoxPlotRatio.png")
            
            self.MessageWarning["text"] = "GC Ratio plotted"
            self.MessageWarning["fg"] = "black"
            self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()
           
        
    def Dinucleotide(self):
        
        if lista:
            self.MessageWarning["text"] = "Loading"
            self.MessageWarning["fg"] = "black"
            self.root.update()
            
            fonte = {'weight':'bold', 'size': 26}
            
            
            dinucleotides =['AA','AC','AG','AT',
                            'CA','CC','CG','CT',
                            'GA','GC','GG','GT',
                            'TA','TC','TG','TT']
            
            for j in range(0, len(lista)):           
                con_dinuc=[] #quantidade total de dinucleotideo
                B= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                din = pd.DataFrame()
                for rec in SeqIO.parse(lista[j],"fasta"):
                    seq_din = rec.seq    
                    all_counts = [] #quantidade de dinucleotideo de cada sequencia
                
                    for dinucleotide in dinucleotides:
                        count = seq_din.count(dinucleotide)
                        all_counts.append(count)
                    con_dinuc = list(map(sum, zip( all_counts, B)))
                    B = con_dinuc
                    din = pd.DataFrame(con_dinuc, index = dinucleotides, columns = [arq_f[j]])
                file = open('Results/Features/Dinucleotides'+ arq_f[j] + '.csv', 'w')
                din.to_csv(r'Results/Features/Dinucleotides'+ arq_f[j] + '.csv', index = True)
                file.close() 
            
                box = []
                plt.style.use(['seaborn-whitegrid']) 
                plt.figure(figsize=(24,12))
                fonte = {'weight':'bold', 'size': 26}
                plt.xlabel("Dinucleotides", fontdict=fonte)
                plt.ylabel("Quantity", fontdict=fonte)
                plt.title("Dinucleotides of " + str(arq_f[j]), fontdict=fonte)
                plt.autoscale()
                
                for aux in range(0, 15):
                    box.append(plt.bar(dinucleotides, con_dinuc,color = "#fc8d62")) ##plot do boxplot
                
                
                
                plt.savefig("Results/Plots/Dinucleotideo"+"_"+str(arq_f[j])+".png")
            
            
            #saving em CSV
            matriz_final = np.zeros(shape=(len(lista),16))
            for j in range(0, len(lista)):           
                con_dinuc=[] #quantidade total de dinucleotideo
                total_arquivo= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                for rec in SeqIO.parse(lista[j],"fasta"):
                    seq_din = rec.seq    
                    all_counts = [] #quantidade de dinucleotideo de cada sequencia
                
                    for dinucleotide in dinucleotides:
                        count = seq_din.count(dinucleotide)
                        all_counts.append(count)
                    con_dinuc = list(map(sum, zip( all_counts, total_arquivo)))
                    total_arquivo = con_dinuc
                matriz_final[j] = total_arquivo
                
            dinuc = pd.DataFrame(matriz_final, index = arq_f, columns = dinucleotides)
            
            file = open('Results/Features/Dinucleotides.csv', 'w')
            dinuc.to_csv(r'Results/Features/Dinucleotides.csv', index = True)
            file.close()
            
            """
            #dinuc.plot(kind='bar', figsize=(24,12))
            plt.xlabel("Dinucleotides", fontdict=fonte)
            plt.ylabel("Quantity", fontdict=fonte)
            plt.title("Dinucleotide", fontdict=fonte)
            plt.tick_params(axis='x', which='major', rotation = 0, labelsize=16)
            plt.legend(fontsize=14)
            
            
            scaler = Normalizer().fit(dinuc)
            scaler_dinuc = scaler.fit_transform(dinuc[arq_f])
            dinuc_scaler = pd.DataFrame(scaler_dinuc, index = dinucleotides, columns = arq_f)
            dinuc_scaler.plot(kind='bar', figsize=(24,12))
            """
            
        
            self.MessageWarning["text"] = "Dinucleotide plotted"
            self.MessageWarning["fg"] = "black"
            self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()
    
        
        
    def Trinucleotide(self):
        
            if lista:
                self.MessageWarning["text"] = "Loading"
                self.MessageWarning["fg"] = "black"
                self.root.update()
                
                #trinucleotides = ['ATC','ATG','ACC','AAC',
                #                 'AAT','AGA','CAT','CAC',
                #                 'CCA','CCG','CGG','CTT',
                #                 'GAT','GTA','GGT','GAA',
                #                 'GCC','GCA','TCA','TAG',
                #                 'TGA','TGG','TGC','TAT']
                
                trinucleotides = ['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 'ATT', 
                                  'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT', 'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT', 
                                  'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT', 
                                  'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT', 'TGA', 'TGC', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT']
                
                for j in range(0, len(lista)):           
                    con_trinuc=[] #quantidade total de dinucleotideo
                    B= [0] * 64
                    trin = pd.DataFrame()
                    for rec in SeqIO.parse(lista[j],"fasta"):
                        seq_din = rec.seq    
                        all_counts = [] #quantidade de trinucleotideo de cada sequencia
                    
                        for trinucleotide in trinucleotides:
                            count = seq_din.count(trinucleotide)
                            all_counts.append(count)
                        con_trinuc = list(map(sum, zip( all_counts, B)))
                        B = con_trinuc
                        trin = pd.DataFrame(con_trinuc, index = trinucleotides, columns = [arq_f[j]])
                    file = open('Results/Features/Trinucleotides'+ arq_f[j] + '.csv', 'w')
                    trin.to_csv(r'Results/Features/Trinucleotides'+ arq_f[j] + '.csv', index = True)
                    file.close() 
                        
                        
                    box = []
                    plt.style.use(['seaborn-whitegrid']) 
                    plt.figure(figsize=(24,12))
                    fonte = {'weight':'bold', 'size': 26}
                    plt.xlabel("Trinucleotides", fontdict=fonte)
                    plt.ylabel("Quantity", fontdict=fonte)
                    plt.title("Trinucleotides of " + str(arq_f[j]), fontdict=fonte)
                    #plt.autoscale()
                    
                    for aux in range(0, 63):
                        box.append(plt.bar(trinucleotides, con_trinuc, color = "#65c2a5")) 
                    
                    plt.xticks(trinucleotides, rotation = 90)
                    plt.savefig("Results/Plots/Trinucleotideo"+"_"+str(arq_f[j])+".png")
                  
                    
                #saving em CSV 
                matriz_final = np.zeros(shape=(len(lista),64))
            
                for j in range(0, len(lista)):           
                    con_trinuc=[] #quantidade total de dinucleotideo
                    total_arquivo= [0]*64
                    for rec in SeqIO.parse(lista[j],"fasta"):
                        seq_trin = rec.seq    
                        all_counts = [] #quantidade de dinucleotideo de cada sequencia
                    
                        for trinucleotide in trinucleotides:
                            count = seq_trin.count(trinucleotide)
                            all_counts.append(count)
                        con_trinuc = list(map(sum, zip( all_counts, total_arquivo)))
                        total_arquivo = con_trinuc
                    matriz_final[j] = total_arquivo
                    
                trinuc = pd.DataFrame(matriz_final, index = arq_f, columns = trinucleotides)
                
                file = open('Results/Features/All_Trinucleotides.csv', 'w')
                trinuc.to_csv(r'Results/Features/All_Trinucleotides.csv', index = True)
                file.close() 
                    
                    
                self.MessageWarning["text"] = "Trinucleotide plotted"
                self.MessageWarning["fg"] = "black"
                self.root.update()
            else:
                self.MessageWarning["text"] = "No file"
                self.MessageWarning["fg"] = "red"
                self.root.update()


    def SaveCsv(self):
        var = len(lista)
        if var ==0: 
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()
        else:
            self.MessageWarning["text"] = "Loading"
            self.MessageWarning["fg"] = "black"
            self.root.update()

            for aux in range(0, len(lista)):
                width = []
                gc_cont = []
                name =[]
                
                nucleotideos =['A','C','G','T']
                GC_ratio = []
    
                
                for rec in SeqIO.parse(lista[aux],"fasta"):
                    seq_nuc = rec.seq    
                    all_counts = [] #quantidade de nucleotideo de cada sequencia
                    for nucleotide in nucleotideos:
                        count = seq_nuc.count(nucleotide)
                        all_counts.append(count)
                    if (all_counts[1]) > 0:    
                        GC_ratio.append(round((all_counts[2])/(all_counts[1]),4))
                    else:
                        GC_ratio.append(all_counts[2])
                    
                
                    width.append(len(rec))
                    width_seq = np.array(width)
                    name.append(rec.id)
                    gc_cont.append(round(GC(rec.seq),4))
                    gc_cont_seq = np.array(gc_cont)
                    GC_ratio_seq = np.array(GC_ratio)
                    
                data = np.array([name, width_seq, gc_cont_seq, GC_ratio_seq]).T
                
                df = pd.DataFrame(data, columns = ['Seq Name','Width', 'GC Content', 'GC Ratio'])
                
                arquivo = open('Results/Features/Features of '+ arq_f[aux] + '.csv', 'w')
                df.to_csv(r'Results/Features/Features of '+ arq_f[aux] + '.csv', index = True)
                arquivo.close()         
        if var >0:    
            self.MessageWarning["text"] = "File saved"
            self.MessageWarning["fg"] = "black"
            self.root.update()
                
    
    def ARFF(self):
        
        self.MessageWarning["text"] = "Loading"
        self.MessageWarning["fg"] = "black"
        self.root.update()
        
        if lista:  
            
            for aux in range(0, len(lista)):
    
                width = []
                gc_cont = []
                name =[]
                
                nucleotideos =['A','C','G','T']
                GC_ratio = []
                
                data = 0
                df = 0
                
                for rec in SeqIO.parse(lista[aux],"fasta"):
                    seq_nuc = rec.seq    
                    all_counts = [] #quantidade de nucleotideo de cada sequencia
                    count = 0
                    for nucleotide in nucleotideos:
                        count = seq_nuc.count(nucleotide)
                        all_counts.append(count)            
                    if (all_counts[1]) > 0:    
                        GC_ratio.append(round((all_counts[2])/(all_counts[1]),4))
                    else:
                        GC_ratio.append(all_counts[2])
                
                    width.append(len(rec))
                    width_seq = np.array(width)
                    name.append(rec.id)
                    gc_cont.append(round(GC(rec.seq),4))
                    gc_cont_seq = np.array(gc_cont)
                    GC_ratio_seq = np.array(GC_ratio)
                    
                data = np.array([name, width_seq, gc_cont_seq, GC_ratio_seq]).T
                
                df = pd.DataFrame(data, columns = ['Seq Name','Width', 'GC Content', 'GC Ratio'])
                
                arff.dump('Results/Features/Result '+ arq_f[aux]+'.arff', df.values, relation = 'relation name', names = ['Seq Name','Width', 'GC Content', 'GC Ratio'])  
                
            self.MessageWarning["text"] = "File saved" 
            self.MessageWarning["fg"] = "black"
            self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()

    
    def DAC(self):
        
        self.MessageWarning["text"] = "Loading"
        self.MessageWarning["fg"] = "black"
        self.root.update()
        
        if(lista):          
            
            DinucIndex =pd.DataFrame([[0.063, 1.502, 0.783, 1.071, -1.376, 0.063, -1.664, 0.783, -0.081, -0.081, 0.063, 1.502, -1.233, -0.081, -1.376, 0.063],
                                      [0.502, 0.502, 0.359,	0.215, -1.364, 1.077, -1.220, 0.359,  0.502,  0.215, 1.077, 0.502, -2.368,  0.502, -1.364, 0.502],
                                      [0.090, 1.190, -0.28,	0.830, -1.010, -0.28, -1.380, -0.28,  0.090,  2.300, -0.28,	1.190, -1.380,	0.090, -1.010,	0.09],
                                      [1.587, 0.126, 0.679,	-1.019,	-0.861,	0.560, -0.822, 0.679, 0.126, -0.348, 0.560, 0.126, -2.243, 	0.126, -0.861, 1.587],
                                      [0.111, 1.289, -0.241, 2.513,	-0.623,	-0.822,	-0.287, -0.241, -0.394, 0.646, -0.822, 1.289, -1.511, -0.394, -0.623, 0.111],
                                      [-0.109, 1.044, -0.623, 1.171, -1.254, 0.242, -1.389, -0.623, 0.711, 1.585, 0.242, 1.044, -1.389, 0.711, -1.254, -0.109]], 
                                     index=['twist', 'tilt', 'roll', 'shift', 'slide', 'rise'], 
                                     columns=['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'CT', 'GA', 'GC', 'GG', 'GT', 'TA', 'TC', 'TG', 'TT'])
        
           
            
            lag = int(self.LagDi.get())
            
            
            if(self.CheckVar2.get()==1 or self.CheckVar3.get()==1 or self.CheckVar4.get()==1 or self.CheckVar5.get()==1 or self.CheckVar6.get()==1 or self.CheckVar7.get()==1):
                if(self.CheckVar2.get()==1):
                    Pu ='twist'
                elif(self.CheckVar3.get()==1):
                    Pu ='tilt'
                elif(self.CheckVar4.get()==1):
                    Pu ='roll'
                elif(self.CheckVar5.get()==1):
                    Pu ='shift'
                elif(self.CheckVar6.get()==1):
                    Pu ='slide'
                elif(self.CheckVar7.get()==1):
                    Pu ='rise'
            
                
                
                for aux in range(0, len(lista)):
                    i=0
                    ListaMedias = []
                    ListaId=[]
                    ListaDAC=[]
                    for rec in SeqIO.parse(lista[aux],"fasta"):
                        
                        PuMedia = 0
                        DAC = 0
                        for j in range(len(rec)-1):
                            PuMedia = PuMedia + (DinucIndex.loc[Pu, rec.seq[j:j+2]])/(len(rec)-1)
                        ListaMedias.append(PuMedia)
          
                            
                        for j in range(len(rec)-lag -1):
                            ComLag = j+lag
                            A=(DinucIndex.loc[Pu, rec.seq[j:j+2]])-ListaMedias[i]
                            B=(DinucIndex.loc[Pu, rec.seq[ComLag:ComLag+2]])-ListaMedias[i]
                            DAC = DAC + ((A)*(B))/(len(rec)-lag-1)
                            
                        i=i+1
                        ListaId.append(rec.id)
                        ListaDAC.append(DAC)
        
                    string = Pu + "- lag" + str(lag)                        
                
                    dacTabela = np.array([ListaId, ListaDAC]).T        
                    dfFinal = pd.DataFrame(dacTabela, columns = ['ID', string])
                    arquivo = open('Results/Features/DAC of '+ arq_f[aux] + '.csv', 'w')
                    dfFinal.to_csv(r'Results/Features/DAC of '+ arq_f[aux] + '.csv', index = True)
                    arquivo.close() 
                    
                self.MessageWarning["text"] = "DAC saved" 
                self.MessageWarning["fg"] = "black"
                self.root.update()
            else:
                self.MessageWarning["text"] = "Chose one Physical Structures"
                self.MessageWarning["fg"] = "red"
                self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()


    def DCC(self):
        self.MessageWarning["text"] = "Loading"
        self.MessageWarning["fg"] = "black"
        self.root.update()
        
        if(lista):          
            
            DinucIndex =pd.DataFrame([[0.063, 1.502, 0.783, 1.071, -1.376, 0.063, -1.664, 0.783, -0.081, -0.081, 0.063, 1.502, -1.233, -0.081, -1.376, 0.063],
                                      [0.502, 0.502, 0.359,	0.215, -1.364, 1.077, -1.220, 0.359,  0.502,  0.215, 1.077, 0.502, -2.368,  0.502, -1.364, 0.502],
                                      [0.090, 1.190, -0.28,	0.830, -1.010, -0.28, -1.380, -0.28,  0.090,  2.300, -0.28,	1.190, -1.380,	0.090, -1.010,	0.09],
                                      [1.587, 0.126, 0.679,	-1.019,	-0.861,	0.560, -0.822, 0.679, 0.126, -0.348, 0.560, 0.126, -2.243, 	0.126, -0.861, 1.587],
                                      [0.111, 1.289, -0.241, 2.513,	-0.623,	-0.822,	-0.287, -0.241, -0.394, 0.646, -0.822, 1.289, -1.511, -0.394, -0.623, 0.111],
                                      [-0.109, 1.044, -0.623, 1.171, -1.254, 0.242, -1.389, -0.623, 0.711, 1.585, 0.242, 1.044, -1.389, 0.711, -1.254, -0.109]], 
                                     index=['twist', 'tilt', 'roll', 'shift', 'slide', 'rise'], 
                                     columns=['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'CT', 'GA', 'GC', 'GG', 'GT', 'TA', 'TC', 'TG', 'TT'])
        
           
            
            lag = int(self.LagDi.get())
            
            
            if((self.CheckVar2.get()==1 and self.CheckVar3.get()==1) 
               or(self.CheckVar2.get()==1 and self.CheckVar4.get()==1) 
               or(self.CheckVar2.get()==1 and self.CheckVar5.get()==1)
               or(self.CheckVar2.get()==1 and self.CheckVar6.get()==1)
               or(self.CheckVar2.get()==1 and self.CheckVar7.get()==1)
               or(self.CheckVar3.get()==1 and self.CheckVar4.get()==1)
               or(self.CheckVar3.get()==1 and self.CheckVar5.get()==1)
               or(self.CheckVar3.get()==1 and self.CheckVar6.get()==1)
               or(self.CheckVar3.get()==1 and self.CheckVar7.get()==1)
               or(self.CheckVar4.get()==1 and self.CheckVar5.get()==1)
               or(self.CheckVar4.get()==1 and self.CheckVar6.get()==1)
               or(self.CheckVar4.get()==1 and self.CheckVar7.get()==1)
               or(self.CheckVar5.get()==1 and self.CheckVar6.get()==1)
               or(self.CheckVar5.get()==1 and self.CheckVar7.get()==1)
               or(self.CheckVar6.get()==1 and self.CheckVar7.get()==1)
               ):
                if(self.CheckVar2.get()==1):
                    Pu1 ='twist'
                    if(self.CheckVar3.get()==1):
                        Pu2 = 'tilt'
                    elif(self.CheckVar4.get()==1):
                        Pu2 ='roll'
                    elif(self.CheckVar5.get()==1):
                        Pu2 ='shift'
                    elif(self.CheckVar6.get()==1):
                        Pu2 ='slide'
                    elif(self.CheckVar7.get()==1):
                        Pu2 ='rise'    
                elif(self.CheckVar3.get()==1):
                    Pu1 ='tilt'
                    if(self.CheckVar4.get()==1):
                        Pu2 ='roll'
                    elif(self.CheckVar5.get()==1):
                        Pu2 ='shift'
                    elif(self.CheckVar6.get()==1):
                        Pu2 ='slide'
                    elif(self.CheckVar7.get()==1):
                        Pu2 ='rise'
                elif(self.CheckVar4.get()==1):
                    Pu1 ='roll'
                    if(self.CheckVar5.get()==1):
                        Pu2 ='shift'
                    elif(self.CheckVar6.get()==1):
                        Pu2 ='slide'
                    elif(self.CheckVar7.get()==1):
                        Pu2 ='rise'
                elif(self.CheckVar5.get()==1):
                    Pu1 ='shift'
                    if(self.CheckVar6.get()==1):
                        Pu2 ='slide'
                    elif(self.CheckVar7.get()==1):
                        Pu2 ='rise'
                elif(self.CheckVar6.get()==1):
                    Pu1 ='slide'
                    Pu2 ='rise'
            
                
                
                for aux in range(0, len(lista)):
                    i=0
                    ListaMedias1 = []
                    ListaMedias2 = []
                    ListaId=[]
                    ListaDCC1=[]
                    ListaDCC2=[]
                    for rec in SeqIO.parse(lista[aux],"fasta"):
                        
                        PuMedia1 = 0
                        PuMedia2 = 0
                        DCC1 = 0
                        DCC2 = 0
                        for j in range(len(rec)-1):
                            PuMedia1 = PuMedia1 + (DinucIndex.loc[Pu1, rec.seq[j:j+2]])/(len(rec)-1)
                        ListaMedias1.append(PuMedia1)
          
                        for j in range(len(rec)-1):
                            PuMedia2 = PuMedia2 + (DinucIndex.loc[Pu2, rec.seq[j:j+2]])/(len(rec)-1)
                        ListaMedias2.append(PuMedia2)
                            
                        for j in range(len(rec)-lag -1):
                            ComLag = j+lag
                            A=(DinucIndex.loc[Pu1, rec.seq[j:j+2]])-ListaMedias1[i]
                            B=(DinucIndex.loc[Pu2, rec.seq[ComLag:ComLag+2]])-ListaMedias2[i]
                            C=(DinucIndex.loc[Pu2, rec.seq[j:j+2]])-ListaMedias2[i]
                            D=(DinucIndex.loc[Pu1, rec.seq[ComLag:ComLag+2]])-ListaMedias1[i]
                            
                            DCC1 = DCC1 + ((A)*(B))/(len(rec)-lag-1)
                            DCC2 = DCC2 + ((C)*(D))/(len(rec)-lag-1)
                            
                        i=i+1
                        ListaId.append(rec.id)
                        ListaDCC1.append(DCC1)
                        ListaDCC2.append(DCC2)
        
                    string1 = Pu1 +"-"+ Pu2 + "- lag" + str(lag)                        
                    string2 = Pu2 +"-"+ Pu1 + "- lag" + str(lag) 
                    
                    dccTabela = np.array([ListaId, ListaDCC1, ListaDCC2]).T        
                    dfFinal = pd.DataFrame(dccTabela, columns = ['ID', string1, string2])
                    arquivo = open('Results/Features/DCC of '+ arq_f[aux] + '.csv', 'w')
                    dfFinal.to_csv(r'Results/Features/DCC of '+ arq_f[aux] + '.csv', index = True)
                    arquivo.close() 
                    
                self.MessageWarning["text"] = "DCC saved" 
                self.MessageWarning["fg"] = "black"
                self.root.update()
            else:
                self.MessageWarning["text"] = "Chose two Physical Structures"
                self.MessageWarning["fg"] = "red"
                self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()


    def TAC(self):
        
        self.MessageWarning["text"] = "Loading"
        self.MessageWarning["fg"] = "black"
        self.root.update()
        
        if(lista):          
            
            TrinucIndex =pd.DataFrame([[-2.087,	-1.509,	-0.506,	-2.126,	0.111,	-0.121,	-0.121,	-1.354,	0.381,	0.304,	-0.313,	-1.354,	1.615,	-0.737,	1.229,	-2.126,	0.265,	0.496,	1.576,	1.229,	-1.856,	0.072,	-0.969,	-0.313,	0.111,	-0.468,	-0.969,	-0.121,	0.882,	0.419,	1.576,	-0.506,	-0.159,	0.034,	0.419,	-0.737,	0.766,	1.036,	-0.468,	0.304,	0.265,	1.036,	0.072,	-0.121,	0.342,	0.034,	0.496,	-1.509,	0.689,	0.342,	0.882,	1.615,	1.730,	0.265,	0.111,	0.381,	1.730,	0.766,	-1.856,	0.111,	0.689,	-0.159,	0.265,	-2.087],
                                      [2.274,	1.105,	0.193,	2.141,	-0.153,	-0.078, -0.074,	0.536,	0.109,	-0.753,	0.039,	0.536,	-0.491,	0.307,	-1.112,	2.141,	0.166,	-0.646,	-0.762,	-1.112,	0.917,	-0.300,	0.558,	0.039,	-0.834,	-0.326,	0.558,	-0.074,	0.062,	-0.365,	-0.762,	0.193,	0.474,	-0.165,	-0.365,	0.307,	-0.702,	-1.687,	-0.326,	-0.753,	0.066,	-1.687,	-0.300,	-0.078,	0.031,	-0.165,	-0.646,	1.105,	0.206,	0.031,	0.062,	-0.491,	-1.103,	0.066,	-0.834,	0.109,	4.522,	-0.702,	0.917,	-0.153,	0.206,	0.474,	0.166,	-2.615]],
                                      index=['Bendability(DNAse)', 'Dnase I'], 
                                      columns=['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 'ATT', 'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT', 'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT', 'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT', 'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT', 'TGA', 'TGC', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT'])
        
           
            
            lag = int(self.LagTri.get())
            if(self.CheckVar8.get()==1 or self.CheckVar9.get()==1):
                if(self.CheckVar8.get()==1):
                    Pu ='Bendability(DNAse)'
                elif(self.CheckVar9.get()==1):
                    Pu ='Dnase I'

            
                
                
                for aux in range(0, len(lista)):
                    i=0
                    ListaMedias = []
                    ListaId=[]
                    ListaTAC=[]
                    for rec in SeqIO.parse(lista[aux],"fasta"):
                        
                        PuMedia = 0
                        TAC = 0
                        for j in range(len(rec)-2):
                            PuMedia = PuMedia + (TrinucIndex.loc[Pu, rec.seq[j:j+3]])/(len(rec)-2)
                        ListaMedias.append(PuMedia)
          
                            
                        for j in range(len(rec)-lag -2):
                            ComLag = j+lag
                            A=(TrinucIndex.loc[Pu, rec.seq[j:j+3]])-ListaMedias[i]
                            B=(TrinucIndex.loc[Pu, rec.seq[ComLag:ComLag+3]])-ListaMedias[i]
                            TAC = TAC + ((A)*(B))/(len(rec)-lag-2)
                            
                        i=i+1
                        ListaId.append(rec.id)
                        ListaTAC.append(TAC)
        
                        
                    TacTabela = np.array([ListaId, ListaTAC]).T        
                    dfFinal = pd.DataFrame(TacTabela, columns = ['ID', Pu + "- lag" + str(lag)])
                    arquivo = open('Results/Features/TAC of '+ arq_f[aux] + '.csv', 'w')
                    dfFinal.to_csv(r'Results/Features/TAC of '+ arq_f[aux] + '.csv', index = True)
                    arquivo.close() 

                self.MessageWarning["text"] = "TAC saved" 
                self.MessageWarning["fg"] = "black"
                self.root.update()
            else:
                self.MessageWarning["text"] = "Chose one Physical Structures"
                self.MessageWarning["fg"] = "red"
                self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()
        
        
    def TCC(self):
        self.MessageWarning["text"] = "Loading"
        self.MessageWarning["fg"] = "black"
        self.root.update()
        
        if(lista):          
            
            TrinucIndex =pd.DataFrame([[-2.087,	-1.509,	-0.506,	-2.126,	0.111,	-0.121,	-0.121,	-1.354,	0.381,	0.304,	-0.313,	-1.354,	1.615,	-0.737,	1.229,	-2.126,	0.265,	0.496,	1.576,	1.229,	-1.856,	0.072,	-0.969,	-0.313,	0.111,	-0.468,	-0.969,	-0.121,	0.882,	0.419,	1.576,	-0.506,	-0.159,	0.034,	0.419,	-0.737,	0.766,	1.036,	-0.468,	0.304,	0.265,	1.036,	0.072,	-0.121,	0.342,	0.034,	0.496,	-1.509,	0.689,	0.342,	0.882,	1.615,	1.730,	0.265,	0.111,	0.381,	1.730,	0.766,	-1.856,	0.111,	0.689,	-0.159,	0.265,	-2.087],
                                      [2.274,	1.105,	0.193,	2.141,	-0.153,	-0.078, -0.074,	0.536,	0.109,	-0.753,	0.039,	0.536,	-0.491,	0.307,	-1.112,	2.141,	0.166,	-0.646,	-0.762,	-1.112,	0.917,	-0.300,	0.558,	0.039,	-0.834,	-0.326,	0.558,	-0.074,	0.062,	-0.365,	-0.762,	0.193,	0.474,	-0.165,	-0.365,	0.307,	-0.702,	-1.687,	-0.326,	-0.753,	0.066,	-1.687,	-0.300,	-0.078,	0.031,	-0.165,	-0.646,	1.105,	0.206,	0.031,	0.062,	-0.491,	-1.103,	0.066,	-0.834,	0.109,	4.522,	-0.702,	0.917,	-0.153,	0.206,	0.474,	0.166,	-2.615]],
                                      index=['Bendability(DNAse)', 'Dnase I'], 
                                      columns=['AAA', 'AAC', 'AAG', 'AAT', 'ACA', 'ACC', 'ACG', 'ACT', 'AGA', 'AGC', 'AGG', 'AGT', 'ATA', 'ATC', 'ATG', 'ATT', 'CAA', 'CAC', 'CAG', 'CAT', 'CCA', 'CCC', 'CCG', 'CCT', 'CGA', 'CGC', 'CGG', 'CGT', 'CTA', 'CTC', 'CTG', 'CTT', 'GAA', 'GAC', 'GAG', 'GAT', 'GCA', 'GCC', 'GCG', 'GCT', 'GGA', 'GGC', 'GGG', 'GGT', 'GTA', 'GTC', 'GTG', 'GTT', 'TAA', 'TAC', 'TAG', 'TAT', 'TCA', 'TCC', 'TCG', 'TCT', 'TGA', 'TGC', 'TGG', 'TGT', 'TTA', 'TTC', 'TTG', 'TTT'])
        
           
            
            lag = int(self.LagTri.get())
            if(self.CheckVar8.get()==1 and self.CheckVar9.get()==1):
                Pu1 ='Bendability(DNAse)'
                Pu2 ='Dnase I'

            
                
                
                for aux in range(0, len(lista)):
                    i=0
                    ListaMedias1 = []
                    ListaMedias2 = []
                    
                    ListaId=[]
                    ListaTCC1=[]
                    ListaTCC2=[]
                    for rec in SeqIO.parse(lista[aux],"fasta"):
                        
                        PuMedia1 = 0
                        PuMedia2 = 0
                        TCC1 = 0
                        TCC2 = 0
                        for j in range(len(rec)-2):
                            PuMedia1 = PuMedia1 + (TrinucIndex.loc[Pu1, rec.seq[j:j+3]])/(len(rec)-2)
                        ListaMedias1.append(PuMedia1)
          
                        for j in range(len(rec)-2):
                            PuMedia2 = PuMedia2 + (TrinucIndex.loc[Pu2, rec.seq[j:j+3]])/(len(rec)-2)
                        ListaMedias2.append(PuMedia2)
                            
                        for j in range(len(rec)-lag -2):
                            ComLag = j+lag
                            A=(TrinucIndex.loc[Pu1, rec.seq[j:j+3]])-ListaMedias1[i]
                            B=(TrinucIndex.loc[Pu2, rec.seq[ComLag:ComLag+3]])-ListaMedias2[i]
                            C=(TrinucIndex.loc[Pu2, rec.seq[j:j+3]])-ListaMedias2[i]
                            D=(TrinucIndex.loc[Pu1, rec.seq[ComLag:ComLag+3]])-ListaMedias1[i]
                            
                            TCC1 = TCC1 + ((A)*(B))/(len(rec)-lag-2)
                            TCC2 = TCC2 + ((C)*(D))/(len(rec)-lag-2)
                            
                        i=i+1
                        ListaId.append(rec.id)
                        ListaTCC1.append(TCC1)
                        ListaTCC2.append(TCC2)
        
                        
                    string1 = Pu1 +"-"+ Pu2 + "- lag" + str(lag)                        
                    string2 = Pu2 +"-"+ Pu1 + "- lag" + str(lag) 
                    TccTabela = np.array([ListaId, ListaTCC1, ListaTCC2]).T        
                    dfFinal = pd.DataFrame(TccTabela, columns = ['ID', string1, string2])
                    arquivo = open('Results/Features/TCC of '+ arq_f[aux] + '.csv', 'w')
                    dfFinal.to_csv(r'Results/Features/TCC of '+ arq_f[aux] + '.csv', index = True)
                    arquivo.close() 
                
                self.MessageWarning["text"] = "TCC saved" 
                self.MessageWarning["fg"] = "black"
                self.root.update()
            else:
                self.MessageWarning["text"] = "Chose two Physical Structures"
                self.MessageWarning["fg"] = "red"
                self.root.update()
        else:
            self.MessageWarning["text"] = "No file"
            self.MessageWarning["fg"] = "red"
            self.root.update()
        
def main(args):
    appProc= Application()
    appProc.execute()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
