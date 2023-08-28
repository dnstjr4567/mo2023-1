using System;
using static System.Console;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using System.Security.Cryptography.X509Certificates;
using System.Linq;
using System.Runtime.InteropServices;
using System.Globalization;
using System.Net.Http.Headers;
#교재 235p 나쁜 이웃집 사람들
namespace ConsoleApp2
{
    class Program
    {

        static void Main(string[] args)
        {
            int[] don1 = { 10, 3, 2, 5, 7, 8 };
            int[] don2 = { 11, 15 };
            int[] don3 = { 7, 7, 7, 7, 7, 7, 7 };
            int[] don4 = { 1, 2, 3, 4, 5, 1, 2, 3, 4, 5 };
            int[] don5 = { 94, 40, 49, 65, 21, 21,106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72 };
            WriteLine(maxDo(don1));
            WriteLine(maxDo(don2));
            WriteLine(maxDo(don3));
            WriteLine(maxDo(don4));
            WriteLine(maxDo(don5));
        }
        public static int maxDo(int[] don)
        {
            int ans = 0;
            int[] dp = new int[don.Length];
            dp[0] = don[0];
            dp[1] = don[1];
            for (int i = 2; i < don.Length-1 ; i++)
            {
               
                dp[i] = Math.Max(don[i] + dp[i-2], dp[i - 1]);
                ///WriteLine($"dp {dp[i]} don{don[i]} i{i}");
            }
            ///WriteLine();
            ans = dp.Max();
            dp[0] = 0;
            for (int i = 2; i < don.Length; i++)
            {
                                
                dp[i] = Math.Max(don[i] + dp[i-2], dp[i - 1]);
                ///WriteLine($"dp {dp[i]} don{don[i]} i{i}");
            }

            ans = Math.Max(ans,dp.Max());
            return ans;
        }


    }
}

//백준 1932 정수삼각형
using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;
using System.Security.Cryptography.X509Certificates;
using System.Configuration;
using System.CodeDom;
using System.Runtime.InteropServices;

namespace ConsoleApp2
{
    internal class Program
    {

        static void Main(string[] args)
        {
            int n = int.Parse(ReadLine());
            int[,] tri = new int[n, n];
            for (int i = 0; i < n; i++)
            {
                int[] arr = Array.ConvertAll(ReadLine().Split(), int.Parse);
                for (int j = 0; j < n; j++)
                {
                    if (j < arr.Length)
                    {
                        tri[i, j] = arr[j];
                    }
                    else
                    {
                        tri[i, j] = -1;
                    }
                }

            }
            
            int[,] sum = new int[n,n];
            sum[0,0] = tri[0, 0];
            int max = sum[0,0];
            for (int i = 1; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (tri[i, j] > -1)
                    {
                        if (j == 0)
                        {
                            sum[i, j] = sum[i - 1, j] + tri[i, j];
                        }
                        else
                        {
                            sum[i, j] = Math.Max(sum[i - 1, j] + tri[i, j], sum[i - 1, j - 1] + tri[i, j]);
                        }
                    }
                    if (sum[i,j]>max)
                    {
                        max = sum[i, j];
                    }
                }
            }
            WriteLine(max);

        }
    }
}
