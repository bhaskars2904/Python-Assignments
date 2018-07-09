package observerworkshop;

public class ForecastDisplay {
    float temperature;
    float humidity;
    float pressure;

    public void update(float temperature, float humidity, float pressure){
        this.humidity = humidity;
        this.pressure = pressure;
        this.temperature = temperature;
        display();
    }
    public void display(){
        System.out.println("Forecast display temperature = "+temperature+", humidity = "+humidity+", pressure = "+pressure);
    }
}
