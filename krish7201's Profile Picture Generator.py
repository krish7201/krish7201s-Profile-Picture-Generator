o
    ` .d�  �                   @   s&   d dl mZ d dlZdd� Ze�  dS )�    )�ImageNc            
   	   C   s�  t jddt�dd�t�dd�t�dd�fd�} t�dd�}d}g }t�dd�t�dd�f}t|�D ]�}t�dd�}t�dd�}t�dd�}t�dd�}g }t|�D ]s}	t�dd�t�dd�f}||v rst�dd�t�dd�f}||v sc|�|� | �|d |d	 f|||f� | �dd|d   |d	 f|||f� | �|d dd|d	   f|||f� | �dd|d   dd|d	   f|||f� qQq1| jd
t jd�} | �	d� | S )NZRGB)�   r   r   ��   )Zcolor�   �   �   �   )�  r	   )Zresamplezprofile_picture.png)
r   �new�randomZrandint�range�appendZputpixelZresizeZBOXZsave)
ZimgZnumIterationsZ	numPixelsZpixelsPlacedZcurPixelZ
iterations�R�G�B�i� r   �(krish7201's Profile Picture Generator.py�newImg   s2   .�
&&0�
r   )ZPILr   r   r   r   r   r   r   �<module>   s    
(