package observerworkshop;

public class WeatherData {
    float temperature;
    float humidity;
    float pressure;
    CurrentConditionsDisplay currentConditionsDisplay = new CurrentConditionsDisplay();
    ForecastDisplay forecastDisplay = new ForecastDisplay();
    public void setMeasurements(float temperature, float humidity, float pressure){
        this.humidity = humidity;
        this.pressure = pressure;
        this.temperature = temperature;
        currentConditionsDisplay.update(temperature, humidity, pressure);
        forecastDisplay.update(temperature, humidity, pressure);
    }
}
