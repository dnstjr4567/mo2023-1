#백준 9461
using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Security.Cryptography.X509Certificates;
using System.Linq;
using System.Runtime.InteropServices;
using System.Globalization;

namespace ConsoleApp2
{
    class Program
    {

        static void Main(string[] args)
        {
            int tc = int.Parse(ReadLine());
            long[] pado = new long[101];
            pado[1] = 1;
            pado[2] = 1;
            pado[3] = 1;
            while (tc > 0)
            {
                int n = int.Parse(ReadLine());
                for (int i = 4; i <= n; i++)
                {
                    pado[i] = pado[i - 3] + pado[i - 2];
                }
                WriteLine(pado[n]);
                
                
                
                tc--;
            }
            
        }



    }
}
#11503
using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Security.Cryptography.X509Certificates;
using System.Linq;
using System.Runtime.InteropServices;
using System.Globalization;

namespace ConsoleApp2
{
    class Program
    {

        static void Main(string[] args)
        {
            int n = int.Parse(ReadLine());
            int[] num = Array.ConvertAll(ReadLine().Split(), int.Parse);
            int[] ans = new int[n];
           
            for (int i = 1; i < n; i++)
            {
             
                for (int j = 0; j < i; j++)
                {
                    if (num[j] < num[i])
                    {
                        ans[i] = Math.Max(ans[i], ans[j] + 1);
                    }
                    
                }

            }
            Write(ans.Max()+1);
        }
    }
}
#1912
using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Security.Cryptography.X509Certificates;
using System.Linq;
using System.Runtime.InteropServices;
using System.Globalization;

namespace ConsoleApp2
{
    class Program
    {

        static void Main(string[] args)
        {
            int n = int.Parse(ReadLine());
            int[] num = Array.ConvertAll(ReadLine().Split(), int.Parse);
            int max = -9999;
            int ans = 0;
            for (int i = 0; i < n; i++)
            {
                if (ans < 0)
                {
                    ans = num[i];
                }
                else if (ans+num[i] < 0)
                {
                    ans = num[i];
                }
                else
                {
                    ans = ans + num[i];
                }
                if (max < ans)
                {
                    max = ans;
                }

            }
            Write(max);
        }



    }
}
#동적 계획법을 공부하고 문제를 해결해보았다
