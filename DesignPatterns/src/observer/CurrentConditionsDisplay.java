package observer;

public class CurrentConditionsDisplay implements Observer, Display {

    private float temperature;
    private float humiidty;
    private float pressure;
    private Subject weatherData;
    public CurrentConditionsDisplay(Subject weatherData){
        this.weatherData = weatherData;
        weatherData.registerObserver(this);
    }
    @Override
    public void display() {
        System.out.println("Current temp and humidity conditions are: temperature = "+temperature+", humidity = "+humiidty);
    }

    @Override
    public void update(float temperature, float humiidty, float pressure) {
        this.humiidty = humiidty;
        this.pressure = pressure;
        this.temperature = temperature;
        display();
    }
}
