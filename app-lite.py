import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="GoKens Bank AI", page_icon="🏦", layout="wide")

st.title("🏦 GoKens Bank AI - Демо версия")
st.subheader("Система персонализированных рекомендаций")

# Демо-данные без тяжелых библиотек
demo_results = [
    {"client_code": 1, "product": "Карта для путешествий", 
     "push_notification": "Айгерим, в январе у вас 12 поездок на такси на 27 400 ₸. С картой для путешествий вернули бы ≈1 100 ₸. Открыть карту."},
    {"client_code": 2, "product": "Премиальная карта",
     "push_notification": "Данияр, у вас стабильно крупный остаток и траты в ресторанах. Премиальная карта даст повышенный кешбэк. Оформить сейчас."},
    {"client_code": 3, "product": "Кредитная карта",
     "push_notification": "Сабина, ваши топ-категории — онлайн, развлечения. Кредитная карта даёт до 10% в любимых категориях. Оформить карту."}
]

# Загрузка CSV или демо
uploaded_file = st.file_uploader("Загрузите CSV с клиентами", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"✅ Загружено {len(df)} клиентов")
    
    if st.button("🚀 Запустить анализ"):
        with st.spinner("Обработка..."):
            # Простая логика без ML
            results = []
            for _, client in df.iterrows():
                # Базовая логика выбора продукта
                if client['avg_monthly_balance_KZT'] > 1000000:
                    product = "Премиальная карта"
                elif client['age'] < 25:
                    product = "Кредитная карта"
                else:
                    product = "Карта для путешествий"
                
                # Генерация уведомления
                notification = f"{client['name']}, у вас есть возможность получить {product}. Оформить?"
                
                results.append({
                    "client_code": client['client_code'],
                    "product": product,
                    "push_notification": notification
                })
            
            # Показ результатов
            results_df = pd.DataFrame(results)
            st.dataframe(results_df)
            
            # Скачивание
            csv = results_df.to_csv(index=False)
            st.download_button("💾 Скачать CSV", csv, "recommendations.csv", "text/csv")
else:
    # Демо-режим
    st.info("📋 Демонстрация с тестовыми данными")
    
    demo_df = pd.DataFrame(demo_results)
    st.dataframe(demo_df)
    
    # Пример уведомления
    st.markdown("### 📱 Пример пуш-уведомления")
    st.info(demo_results[0]['push_notification'])