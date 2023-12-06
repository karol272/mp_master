#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Proyecto Prueba


# In[7]:


#librerias
import tkinter as tk


# In[8]:


# Crear la ventana principal
ventana = tk.Tk()


# In[9]:


# Definir la función que se ejecutará cuando se haga clic en el botón
def enviar_datos():
    print("Items:", items.get())
    print("Descripcion_Item:", descripcion_item.get())
    print("Bodega:", bodega.get())
    print("Proveedor:", proveedor.get())
    print("Vendedor:", vendedor.get())
    


# In[10]:


# Crear los widgets del formulario
tk.Label(ventana, text="Items:").grid(row=0, column=0)
items = tk.Entry(ventana)
items.grid(row=0, column=1)

tk.Label(ventana, text="Descripcion_Item:").grid(row=1, column=0)
descripcion_item = tk.Entry(ventana)
descripcion_item.grid(row=1, column=1)

tk.Label(ventana, text="Bodega:").grid(row=2, column=0)
bodega = tk.Entry(ventana)
bodega.grid(row=2, column=1)

tk.Label(ventana, text="Proveedor:").grid(row=3, column=0)
proveedor = tk.Entry(ventana)
proveedor.grid(row=3, column=1)
 
tk.Label(ventana, text="Vendedor:").grid(row=4, column=0)
vendedor = tk.Entry(ventana)
vendedor.grid(row=4, column=1)
 
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_datos)
boton_enviar.grid(row=5, column=0, columnspan=2)


# In[11]:
# Prueba3
# Mostrar la ventana
ventana.mainloop()

