import streamlit as st
from PIL import Image
import style_transfer as style


# def get_image_download_link(img):
#     """Generates a link allowing the PIL image to be downloaded
# 	in:  PIL image
# 	out: href string
# 	"""
#     buffered = BytesIO()
#     img.save(buffered, format="JPEG")
#     img_str = base64.b64encode(buffered.getvalue()).decode()
#     href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>'
#     return href
#
#
# st.markdown(get_image_download_link(result), unsafe_allow_html=True)


def main():
    st.set_page_config(layout="centered")
    st.title('Нейронный перенос стиля')
    # st.text(tf.executing_eagerly())
    menu = ["Домашняя страница", "Обо мне"]
    choice = st.sidebar.selectbox("Меню", menu)

    if choice == "Домашняя страница":
        st.subheader("Выберите два изображения:")
        col1, col2 = st.beta_columns(2)

        with col1:
            content_image = st.file_uploader("Выберите изображение для обработки", ['png', 'jpg', 'jpeg'],
                                             help="Перетащите или выберите файл, "
                                                  "ограничение размера - 25 Мб на файл\n\n"
                                                  " • Форматы файлов - PNG, JPG, JPEG.")
            if content_image is not None:
                col1.image(content_image, use_column_width=True)

        with col2:
            style_image = st.file_uploader("Выберите изображение с исходным стилем", ['png', 'jpg', 'jpeg'],
                                           help="Перетащите или выберите файл, "
                                                "ограничение размера - 25 МБ на файл\n\n"
                                                " • Форматы файлов - PNG, JPG, JPEG.")
            if style_image is not None:
                col2.image(style_image, use_column_width=True)

        col4, col5, col6 = st.beta_columns((1, 3, 1))
        with col5:
            number_of_iterations = st.slider("Выберите число итераций цикла стилизации", 10, 500, 20, 1,
                                             format=None, key=None,
                                             help="Число итераций определяет итоговое качество стилизации изображения")

        col7, col8, col9 = st.beta_columns((2, 1, 2))
        with col8:
            style_transfer_button = st.button("Начать перенос стиля")
        # with col9:
        #     end_button = st.button("Stop")

        if style_transfer_button:
            if content_image is not None and style_image is not None:
                best, best_loss = style.run_style_transfer(content_image, style_image, number_of_iterations)
                # if end_button:
                #     pass
                col10, col11, col12 = st.beta_columns((1, 4, 1))
                with col11:
                    if best.any():
                        col11.image(Image.fromarray(best), use_column_width=True)
            elif content_image is not None:
                st.error("Ошибка: Изображение с исходным стилем не загружено.")
            elif style_image is not None:
                st.error("Ошибка: Изображение для обработки не загружено.")
            else:
                st.error("Ошибка: Изображение для обработки и изображение с исходным стилем не загружены.")
    else:
        st.subheader("Обо мне")
        st.text("Журавлева Полина, ИУ5-81Б")
        st.text("2021")


if __name__ == '__main__':
    main()
