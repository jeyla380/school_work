package Final;

public class DemoEnum {

    enum DayOfTheWeek{

        SU,
        MO,
        TU,
        WE,
        TH,
        FR,
        SA;
    }

    public static void main(String[] args){
        DayOfTheWeek firstDay = DayOfTheWeek.SU;
        System.out.printf("First Day: %s", firstDay);
        System.out.println();

        for(DayOfTheWeek days : DayOfTheWeek.values()){
            System.out.printf("%s ", days);
        }
    }
}
