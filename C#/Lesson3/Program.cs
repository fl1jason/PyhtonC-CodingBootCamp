using System;

namespace Lesson3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Now for some For and While Loops!");

            Console.WriteLine("So...how many bottles of coke shall we drink? Enter a number:");

            string strInput = Console.ReadLine();

            int nBottles = int.Parse(strInput);

            if (nBottles > 10)
            {
                Console.WriteLine(string.Format("Woah, {0}, that's a lot of bottles!", nBottles.ToString()));
            }
            else
            {
                Console.WriteLine("Let's have a drink using a While Loop");

                int nBottle = 1;
                while (nBottle <= nBottles)
                {
                    Console.WriteLine(string.Format("Drinking {0} bottle of coke", nBottle.ToString()));
                    nBottle++;
                }

                Console.WriteLine("Let's have a drink using a For Loop");

                for (int nBottleNo = 1; nBottleNo <= nBottles; nBottleNo++)
                {
                    Console.WriteLine(string.Format("Drinking {0} bottle of coke", nBottleNo.ToString()));
                }

                Console.WriteLine("Let's do this the other way round");

                for (int nBottleNo = nBottles; nBottleNo >= 0; nBottleNo--)
                {
                    Console.WriteLine(string.Format("Drinking {0} bottle of coke", nBottleNo.ToString()));
                }

                Console.WriteLine("How about counting in two?");

                for (int nBottleNo = 1; nBottleNo <= nBottles; nBottleNo+=2)
                {
                    Console.WriteLine(string.Format("Drinking {0} bottle of coke", nBottleNo.ToString()));
                }
            }
        }
    }
}
