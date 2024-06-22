import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

#temperature data
temp = [36,37,37,38,38,37,35,33,31,30,29,28,27,26,25,25,24,24,23,24,26,29,32,34,35]
weather_conditions = ['sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny', 'cloudy', 'cloudy', 'cloudy', 'rainy', 'rainy', 'rainy', 'rainy', 'rainy', 'rainy', 'mixed', 'mixed', 'mixed', 'cloudy', 'cloudy', 'sunny', 'sunny', 'sunny', 'sunny', 'sunny']

#ARIMA MODEL
model = ARIMA(temp, order=(5,1,0))
model_fit = model.fit()

forecast = model_fit.forecast(steps=25)

#moving avg
def moving_average(data, window_size):
    moving_avg = np.convolve(data, np.ones(window_size)/window_size, mode='valid')
    return np.concatenate((data[:window_size-1], moving_avg))

predicted_days = np.arange(len(temp) + 1, len(temp) + 26)
window_size = 3
predicted_temperature = moving_average(temp, window_size)

#actual data
plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, len(temp) + 1), temp, marker='o', color='b', label='Actual Temperature (°C)')
plt.scatter(np.arange(1, len(temp) + 1), temp, color='black', marker='o', label='Weather Condition')

#forecasted data
forecast_weather_conditions = ['sunny'] * 7 + ['sunny'] * 7 + ['rainy'] * 5 + ['mixed'] * 4 + ['cloudy'] * 2
plt.scatter(np.arange(len(temp) + 1, len(temp) + 26), forecast, color='black', marker='o', label='Weather Condition (Forecast)', zorder=5)
for i, txt in enumerate(forecast_weather_conditions):
    plt.annotate(txt, (np.arange(len(temp) + 1, len(temp) + 26)[i], forecast[i] + 0.5), textcoords="offset points", xytext=(0,5), ha='center', zorder=6)




    

plt.plot(np.arange(len(temp) + 1, len(temp) + 26), forecast, marker='o', linestyle='--', color='r', label='Forecasted Temperature (°C)')

plt.plot(predicted_days, predicted_temperature, marker='o', linestyle='--', color='green', label=f'Predicted Temperature (°C)')

plt.grid(True)
plt.legend()
plt.xticks(np.arange(1, len(temp) + 26))
plt.tight_layout()
plt.xlabel('days')
plt.ylabel('temperature')
plt.title('Weather Forecast')
plt.legend()
plt.show()


