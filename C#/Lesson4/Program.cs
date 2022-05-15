using System;
using System.

namespace Lesson4
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Let's have a go at Switch Statements");

            Console.WriteLine("Give me a day of the week: ");

            string strInput = Console.ReadLine();

            switch (strInput.ToLower())
            {
                case "monday":
                    Console.WriteLine("Nah, Monday's are back to school days!");
                    break;
                case "tuesday":
                    Console.WriteLine("mmmm, pancakes!");
                    break;
                case "wednesday":
                    Console.WriteLine("Half way through the week!");
                    break;
                case "thursday":
                    Console.WriteLine("...is the new Friday!");
                    break;
                case "friday":
                    Console.WriteLine("most awesome day of the week!");
                    break;
                case "saturday":
                    Console.WriteLine("shopping and partying!");
                    break;
                case "sunday":
                    Console.WriteLine("sleeping and eating!");
                    break;
                default:
                    Console.WriteLine("Say what?");
                    break;

            }
        }
    }
}
