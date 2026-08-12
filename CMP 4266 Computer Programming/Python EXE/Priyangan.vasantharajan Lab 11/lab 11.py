# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:30:06 2026

@author: Priyangan
"""

import tkinter

class Calculator_GUI:
    
    def __init__(self):
        self.mw = tkinter.TK()
        self.mw.title("Calculator")
        
        self.top_frame = tkinter.Frame(self.mw)
        self.mid.frame = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)
        
        self.entry_label = tkinter = tkinter.Label(self.top_frame, text="Enter Numbers:")
        self.entry = tkinter.Entry(self.top_frame, width = 25)
        
        self.entry_label.pack(side = "left")
        self.entry.pack(side="left")
        
        
        self.add_button=tkinter.Button(self.bottom_frame,text="+", command =self.add)
        self.substract_button=tkinter.Button(self.bottom_frame,text="-", command =self.substract)
        self.rest_button=tkinter.Button(self.bottom_frame,text="Reset", command =self.reset)
        
        
        