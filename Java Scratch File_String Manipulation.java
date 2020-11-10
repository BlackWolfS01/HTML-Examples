import java.util.Scanner;
class Scratch {
     public static void main ( String[] args ) {
          //String Manipulation
          Scanner scanner = new Scanner(System.in);

          /*
          While Loop:
          It allows the program to run constantly until the user
          choices to end the session.
           */
          while(true)
          {
               //
               String message =  scanner.nextLine();
               System.out.println(message);
               if(message.toLowerCase ().equals( "quit")){
                    break;
               }

          }
          scanner.close();
     }
}
