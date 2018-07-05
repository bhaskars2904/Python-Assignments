package observer;

import java.util.ArrayList;
import java.util.List;

public class WeatherData implements Subject {
    private float temperature;
    private float humiidty;
    private float pressure;
    private List<Observer> observers;

    public WeatherData(){
        observers = new ArrayList<Observer>();
    }

    @Override
    public void registerObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        int i = observers.indexOf(observer);
        if(i>=0){
            observers.remove(observer);
        }
    }

    @Override
    public void notifyObservers() {
        for(Observer o: observers) {
            o.update(temperature, humiidty, pressure);
        }
    }

    public void setMeasurements(float temperature, float humiidty, float pressure){
        this.humiidty = humiidty;
        this.pressure = pressure;
        this.temperature = temperature;
        notifyObservers();
    }
}
