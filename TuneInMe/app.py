import streamlit as st

# === Ruh Hali Sınıfları ===
class Mood:
    def __init__(self, user_description):
        self.user_description = user_description

    def recommend(self):
        raise NotImplementedError

    def respond(self):
        raise NotImplementedError


class Happy(Mood):
    def recommend(self):
        return "La La Land"

    def respond(self):
        return (
            f"Ne güzel! 😊 Enerjin çok yüksek hissediliyor. "
            f"Modunu daha da yükseltecek bir film önerim var: **{self.recommend()}**. "
            f"Müzikleri, renkleri ve danslarıyla tam senlik. Keyfini çıkar!"
        )


class Sad(Mood):
    def recommend(self):
        return "The Pursuit of Happyness"

    def respond(self):
        return (
            f"Üzgün hissettiğini söyledin. Bu çok insani bir duygu. "
            f"Sana umut verecek bir film öneriyorum: **{self.recommend()}**. "
            f"Zor zamanlarda bile güçlü kalabilmeyi anlatan dokunaklı bir hikaye."
        )


class Stressed(Mood):
    def recommend(self):
        return "Forrest Gump"

    def respond(self):
        return (
            f"Stresli bir dönem geçiriyorsun gibi görünüyor. "
            f"Böyle zamanlarda sade ve ilham verici bir film iyi gelir: **{self.recommend()}**. "
            f"Belki hayatın hızını biraz yavaşlatabilir."
        )


class Excited(Mood):
    def recommend(self):
        return "Mad Max: Fury Road"

    def respond(self):
        return (
            f"Harika! Bu enerjiyi bir yere kanalize etmek lazım. "
            f"Adrenalin dolu bir önerim var: **{self.recommend()}**. "
            f"Aksiyon sever biri olarak çok beğeneceğini düşünüyorum!"
        )


class Tired(Mood):
    def recommend(self):
        return "The Secret Life of Walter Mitty"

    def respond(self):
        return (
            f"Yorgun hissediyorsan zihnini biraz hayallere bırakmanın zamanı gelmiştir. "
            f"**{self.recommend()}** seni içsel bir yolculuğa çıkarabilir. 🌍"
        )


class InLove(Mood):
    def recommend(self):
        return "Pride and Prejudice"

    def respond(self):
        return (
            f"Aşık olmak ne güzel bir duygu! Kalbinin ritmine uygun bir film: **{self.recommend()}**. "
            f"Tutku ve zarafet dolu klasik bir aşk hikayesi seni bekliyor. 💖"
        )


class Calm(Mood):
    def recommend(self):
        return "Amélie"

    def respond(self):
        return (
            f"Sakinlik huzur verir. Bu duyguyu bozmadan içten bir filmle devam edelim: **{self.recommend()}**. "
            f"**Amélie**, küçük mutlulukların gücünü hatırlatacak."
        )


# === Ruh Hali Anahtar Kelimeleri ===
MOOD_KEYWORDS = {
    "Mutlu": ["mutlu", "iyi", "harika", "neşeli", "şahane", "pozitif"],
    "Üzgün": ["üzgün", "mutsuz", "kötü", "yalnız", "moralsiz", "keyifsiz"],
    "Stresli": ["stresli", "baskı", "gergin", "yoğun"],
    "Heyecanlı": ["heyecan", "sabırsız", "coşkulu", "kıpır kıpır"],
    "Yorgun": ["yorgun", "bitkin", "uykusuz", "tükenmiş"],
    "Aşık": ["aşık", "kalp", "sevgili", "romantik"],
    "Sakin": ["sakin", "huzurlu", "dingin", "sessiz"]
}

def detect_mood_from_text(user_input):
    user_input = user_input.lower()
    for mood, keywords in MOOD_KEYWORDS.items():
        for keyword in keywords:
            if keyword in user_input:
                return mood
    return "Sakin"  # varsayılan

# === Mood sınıfları sözlüğü ===
mood_classes = {
    "Mutlu": Happy,
    "Üzgün": Sad,
    "Stresli": Stressed,
    "Heyecanlı": Excited,
    "Yorgun": Tired,
    "Aşık": InLove,
    "Sakin": Calm
}

# === Streamlit Arayüzü ===
st.set_page_config(page_title="TuneInMe", layout="centered")
st.title("🎬 TuneInMe – Duygusal Film Asistanın")

user_input = st.text_input("Bugün nasılsın? Anlat, seni dinliyorum:")

if st.button("🎥 Film Öner"):
    if user_input.strip():
        mood = detect_mood_from_text(user_input)
        mood_class = mood_classes[mood]
        mood_instance = mood_class(user_input)
        st.success(f"🔍 Ruh halin: **{mood}**")
        st.write(mood_instance.respond())
    else:
        st.warning("Lütfen nasıl hissettiğini yaz :)")

