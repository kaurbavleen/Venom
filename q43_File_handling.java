import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/*  WAP to implement file handling . The program should copy 
    the content from one file to another. */

public class q43_File_handling 
{
    public static void main(String[] args) 
    {
        FileReader reader = null;
        FileWriter writer = null;

        try 
        {
            // Open the source file for reading
            reader = new FileReader("q1_greatest_number.txt");

            // Open the destination file for writing
            writer = new FileWriter("copy.txt");

            int character;
            
            // Read each character from source and write to destination
            while ((character = reader.read()) != -1) 
            {
                writer.write(character);
            }

            System.out.println("File copied successfully!");
        } 
        catch (IOException e) 
        {
            System.out.println("An error occurred during file handling: " + e.getMessage());
        } 
        finally 
        {
            try 
            {
                if (reader != null) 
                {
                    reader.close(); // Closing source file
                }
                if (writer != null) 
                {
                    writer.close(); // Closing destination file
                }
            } 
            catch (IOException e) 
            {
                System.out.println("Error while closing files: " + e.getMessage());
            }
        }
    }    
}
