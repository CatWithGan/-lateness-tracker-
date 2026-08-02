import os
import json
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

# Задаем темно-серый фон приложения
Window.clearcolor = (0.12, 0.12, 0.12, 1)

# Вспомогательный класс для создания красивых закругленных карточек
class CardLayout(BoxLayout):
    def __init__(self, bg_color=(0.18, 0.18, 0.20, 1), **kwargs):
        super().__init__(**kwargs)
        self.padding = 15
        self.spacing = 10
        self.orientation = 'vertical'
        self.size_hint_y = None
        with self.canvas.before:
            Color(*bg_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[12])
        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class LatenessApp(App):
    def build(self):
        self.title = 'Детектор Опозданий'
        self.data_file = os.path.join(self.user_data_dir, 'lateness_data.json')
        self.data = self.load_data()

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Заголовок
        header = Label(
            text="⏱️ Детектор Опозданий",
            font_size='22sp',
            bold=True,
            size_hint_y=None,
            height=50,
            color=(0.8, 0.5, 1, 1)
        )
        main_layout.add_widget(header)

        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', spacing=15, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        # --- КАРТОЧКА 1: Новый замер ---
        card1 = CardLayout(height=230)
        card1.add_widget(Label(text="➕ Внести новый приезд", font_size='18sp', bold=True, size_hint_y=None, height=30))
        
        self.in_promised = TextInput(hint_text="Обещал приехать через (мин)", multiline=False, input_filter='float', size_hint_y=None, height=40)
        self.in_actual = TextInput(hint_text="Реально приехал через (мин)", multiline=False, input_filter='float', size_hint_y=None, height=40)
        
        btn_save = Button(text="СОХРАНИТЬ", size_hint_y=None, height=45, background_color=(0.5, 0.2, 0.8, 1))
        btn_save.bind(on_release=self.add_entry)
        
        card1.add_widget(self.in_promised)
        card1.add_widget(self.in_actual)
        card1.add_widget(btn_save)
        content.add_widget(card1)

        # --- КАРТОЧКА 2: Прогноз ---
        card2 = CardLayout(height=200)
        card2.add_widget(Label(text="🔮 Калькулятор Реальности", font_size='18sp', bold=True, size_hint_y=None, height=30))
        
        self.in_predict = TextInput(hint_text="Друг говорит: 'Буду через...' (мин)", multiline=False, input_filter='float', size_hint_y=None, height=40)
        self.lbl_predict = Label(text="Введите время для расчета", size_hint_y=None, height=30, color=(0.7, 0.7, 0.7, 1))
        
        btn_predict = Button(text="РАССЧИТАТЬ", size_hint_y=None, height=45, background_color=(0.2, 0.6, 0.8, 1))
        btn_predict.bind(on_release=self.calculate)
        
        card2.add_widget(self.in_predict)
        card2.add_widget(btn_predict)
        card2.add_widget(self.lbl_predict)
        content.add_widget(card2)

        # --- КАРТОЧКА 3: Статистика ---
        card3 = CardLayout(height=160)
        card3.add_widget(Label(text="📊 Статистика", font_size='18sp', bold=True, size_hint_y=None, height=30))
        
        self.lbl_count = Label(text="Замеров: 0", size_hint_y=None, height=25)
        self.lbl_delay = Label(text="Среднее опоздание: --", size_hint_y=None, height=25)
        self.lbl_ratio = Label(text="Замедление: --", size_hint_y=None, height=25)
        
        card3.add_widget(self.lbl_count)
        card3.add_widget(self.lbl_delay)
        card3.add_widget(self.lbl_ratio)
        content.add_widget(card3)

        scroll.add_widget(content)
        main_layout.add_widget(scroll)

        self.update_ui()
        return main_layout

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)

    def add_entry(self, instance):
        if not self.in_promised.text or not self.in_actual.text:
            return
        try:
            promised = float(self.in_promised.text)
            actual = float(self.in_actual.text)
        except ValueError:
            return

        delay = actual - promised
        ratio = actual / promised if promised > 0 else 1.0

        self.data.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "promised": promised,
            "actual": actual,
            "delay": delay,
            "ratio": ratio
        })
        self.save_data()
        
        self.in_promised.text = ""
        self.in_actual.text = ""
        self.update_ui()

    def calculate(self, instance):
        if not self.in_predict.text or not self.data:
            self.lbl_predict.text = "Сначала добавьте замеры!"
            return
        try:
            promised = float(self.in_predict.text)
        except ValueError:
            return

        total = len(self.data)
        avg_delay = sum(x['delay'] for x in self.data) / total
        avg_ratio = sum(x['ratio'] for x in self.data) / total

        predicted = (promised * avg_ratio + (promised + avg_delay)) / 2
        self.lbl_predict.text = f"Приедет через ~{predicted:.0f} мин (опоздание ~{predicted - promised:.0f} мин)"

    def update_ui(self):
        if not self.data:
            return
        total = len(self.data)
        avg_delay = sum(x['delay'] for x in self.data) / total
        avg_ratio = sum(x['ratio'] for x in self.data) / total

        self.lbl_count.text = f"Всего замеров: {total}"
        self.lbl_delay.text = f"Среднее опоздание: {avg_delay:+.1f} мин"
        self.lbl_ratio.text = f"Коэффициент замедления: {avg_ratio:.2f}x"

if __name__ == '__main__':
    LatenessApp().run()