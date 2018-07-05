package observer;

public class ForecastDisplay implements Observer, Display {

    private float temperature;
    private float humiidty;
    private float pressure;
    private Subject weatherData;
    ForecastDisplay(Subject weatherData){
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }
    @Override
    public void display() {
        System.out.println("Forecast conditions are temperature = "+temperature+", pressure = "+pressure);
    }

    @Override
    public void update(float temperature, float humiidty, float pressure) {
       this.temperature = temperature;
       this.pressure = pressure;
       display();
    }
}
