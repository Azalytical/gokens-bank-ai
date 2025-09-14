import os
import streamlit as st

# Проверка окружения
IS_CLOUD = os.getenv('STREAMLIT_SHARING_MODE', '') == 'true'

if IS_CLOUD:
    st.info("🌐 Запущено на Streamlit Cloud")
    
    # Опция загрузки данных через интерфейс
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    
    if not st.session_state.data_loaded:
        st.warning("📁 Пожалуйста, загрузите CSV файлы")
        
        uploaded_files = st.file_uploader(
            "Загрузите CSV файлы",
            type=['csv'],
            accept_multiple_files=True
        )
        
        if uploaded_files:
            # Сохранение загруженных файлов
            os.makedirs('data', exist_ok=True)
            for file in uploaded_files:
                with open(f"data/{file.name}", "wb") as f:
                    f.write(file.getbuffer())
            
            st.session_state.data_loaded = True
            st.success(f"✅ Загружено {len(uploaded_files)} файлов")
            st.rerun()
else:
    # Локальный запуск
    st.info("💻 Локальный режим")