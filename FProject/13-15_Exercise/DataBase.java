package 13-15_Exercise;

import java.util.Collection;

public interface DataBase <T>{

    void add(T item);


    Collection<T> getAll();

}