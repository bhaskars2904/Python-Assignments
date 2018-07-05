package observer;

public class ObserverPatternDemo {
    public static void main(String[] args) {
        WeatherData weatherData = new WeatherData();
        CurrentConditionsDisplay currentConditionsDisplay = new CurrentConditionsDisplay(weatherData);
        ForecastDisplay forecastDisplay = new ForecastDisplay(weatherData);
        weatherData.setMeasurements(1.0f,2.0f,3.0f);
        weatherData.setMeasurements(5.0f, 8, 9);
        weatherData.removeObserver(currentConditionsDisplay);
        weatherData.setMeasurements(5,6.2f,8);

    }
}
