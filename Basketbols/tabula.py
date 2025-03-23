import pandas as pd
import matplotlib.pyplot as plt

# === 1. Nolasīt datus no JSON ===
df = pd.read_json('data.json')

# === 2. Saglabāt mēnešu secību ===
months_lv_order = [
    'Janvāris', 'Februāris', 'Marts', 'Aprīlis', 'Maijs', 'Jūnijs',
    'Jūlijs', 'Augusts', 'Septembris', 'Oktobris', 'Novembris', 'Decembris'
]
df['menesis'] = pd.Categorical(df['menesis'], categories=months_lv_order, ordered=True)

# === 3. Izveidot unikālu spēlētāja identifikatoru (vārds + uzvārds) ===
df['speletajs'] = df['vards'] + ' ' + df['uzvards']

# === 4. Grupēt datus pēc spēlētāja un mēneša, aprēķināt vidējo punktu skaitu (ja vairākas spēles mēnesī) ===
df_avg = df.groupby(['speletajs', 'menesis'])['punkti'].mean().reset_index()

# === 5. Zīmēt grafiku ar dažādām krāsām katram spēlētājam ===
plt.figure(figsize=(14, 7))

for speletajs in df_avg['speletajs'].unique():
    dati = df_avg[df_avg['speletajs'] == speletajs]
    plt.plot(dati['menesis'], dati['punkti'], marker='o', label=speletajs)

    # Pievienot punktu vērtības uz līnijas
    for i in range(len(dati)):
        plt.text(dati['menesis'].iloc[i], dati['punkti'].iloc[i] + 0.5,
                 f"{dati['punkti'].iloc[i]:.1f}", ha='center', fontsize=8)

# === 6. Noformēt grafiku ===
plt.title('Vidējie punkti par spēli katram spēlētājam mēnešos')
plt.xlabel('Mēnesis')
plt.ylabel('Vidējie punkti')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Spēlētāji', loc='upper left')
plt.tight_layout()

# === 7. Parādīt grafiku ===
plt.show()
