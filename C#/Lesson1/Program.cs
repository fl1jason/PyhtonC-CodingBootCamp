using System;

namespace Lesson
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("Welcome!");

            // Ask for te user's name
            Console.WriteLine("I'm C#, what's your name?");
            string name = Console.ReadLine();
            
            Console.WriteLine("Hi " + name + ", how you doing today?");
        }
    }
}
