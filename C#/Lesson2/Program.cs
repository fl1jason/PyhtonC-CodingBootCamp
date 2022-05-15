using System;
using System.Text;

namespace Lesson2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Add two numbers...");

            Console.WriteLine("Please enter your first number: ");
            string strInput = Console.ReadLine();

            Int32 nFirstNumber = 0;
            if (!IsNumeric(strInput))
            {
                Console.WriteLine("your first number must be a numeric value");
            }
            else
            {
                nFirstNumber = Int32.Parse(strInput);
            }

            Console.WriteLine("Please enter your second number: ");
            strInput = Console.ReadLine();

            Int32 nSecondNumber = 0;
            if (!IsNumeric(strInput))
            {
                Console.WriteLine("your second number must be a numeric value");
            }
            else
            {
                nSecondNumber = Int32.Parse(strInput);
            }

            // Calculate the result
            Int32 nResult = nFirstNumber + nSecondNumber;

            Console.WriteLine("Answer: " + nResult.ToString());
        }

        static bool IsNumeric(string value)
        {
            Int32 test = 0;
            bool bSucceeded = Int32.TryParse(value, out test);

            return (bSucceeded);
        }
    }
}
