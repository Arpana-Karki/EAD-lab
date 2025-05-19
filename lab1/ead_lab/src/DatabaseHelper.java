// Singeleton Pattern

public class DatabaseHelper{
    private static DatabaseHelper instance;

    private DatabaseHelper(){}

    public  static DatabaseHelper getInstance(){
        if(instance == null){
            instance = new DatabaseHelper();

        }
        return instance;
    }
}


