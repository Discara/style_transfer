import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

import tensorflow as tf
from tensorflow.python.keras.preprocessing import image as kp_image
import style_transfer as style


def main():
    st.set_page_config(layout="wide")
    st.title('Нейронный перенос стиля')
    # st.text(tf.executing_eagerly())
    menu = ["Домой", "Обо мне"]
    choice = st.sidebar.selectbox("Меню", menu)

    if choice == "Домой":
        st.subheader("Выберите два изображения:")
        col1, col2 = st.beta_columns(2)

        with col1:
            content_image = st.file_uploader("Выберите изображение содержания", ['png', 'jpg', 'jpeg'],
                                             help="Перетащите или выберите файл. \n\n"
                                                  "Ограничение размера - 200 МБ на файл\n\n"
                                                  "• Форматы файлов - PNG, JPG, JPEG.")
            if content_image is not None:
                col1.image(content_image, use_column_width=True)

        with col2:
            style_image = st.file_uploader("Выберите изображение стиля", ['png', 'jpg', 'jpeg'],
                                           help="Перетащите или выберите файл, ограничение размера - 200 МБ на "
                                                "файл • Форматы файлов - PNG, JPG, JPEG.")
            if style_image is not None:
                col2.image(style_image, use_column_width=True)

        col4, col5, col6 = st.beta_columns(3)
        with col5:
            number_of_iterations = st.slider("Выберите число итераций цикла стилизации", 10, 200, 20, 1,
                                             format=None, key=None,
                                             help="Число итераций определяет итоговое качество стилизации изображения")

        col4, col5, col6 = st.beta_columns((4, 1, 4))
        with col5:
            style_transfer_button = st.button("Run style transfer")

        if style_transfer_button:
            if content_image is not None and style_image is not None:
                best, best_loss = style.run_style_transfer(content_image, style_image, number_of_iterations)
                col7, col8, col9 = st.beta_columns(3)
                with col8:
                    if best.any():
                        col8.image(Image.fromarray(best), use_column_width=True)
            else:
                st.error("Ошибка: Хотя бы одно изображение не загружено.")
    else:
        st.subheader("Обо мне")


if __name__ == '__main__':
    main()
