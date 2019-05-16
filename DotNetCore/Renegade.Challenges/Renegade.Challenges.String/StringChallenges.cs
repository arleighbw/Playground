using System;
using System.Collections.Generic;
using System.Text;

namespace Renegade.Challenges.String
{
    public static class StringChallenges
    {
        public static int CountMessageInterference(string s, string targetMessage)
        {
            var count = 0;
            var templateSize = targetMessage.Length;

            for (int i = 0; i < s.Length; i++)
            {
                if (!s[i].Equals(targetMessage[i % templateSize])) count++; 
            }

            return count;
        }

        public static long RepeatedStringSearchOccurences(string s, long n)
        {
            if (s.Length == 1 && s[0].Equals('a')) return n;

            var countByIndex = new List<int>();

            for (int i = 0; i < s.Length; i++)
            {
                if (s[i % s.Length].Equals('a'))
                {
                    countByIndex.Add(i);
                }
            }

            var iterations = n / s.Length;
            var iterationsCount = iterations * countByIndex.Count;

            var modIndex = n % s.Length - 1;
            var modCount = 0;
            foreach (var index in countByIndex)
            {
                if (index <= modIndex) modCount++;
                else
                {
                    continue;
                }
            }

            return iterationsCount + modCount;
        }

        public static string TimeConversion(string s)
        {
            var timeFormat = 12;
            var hour = 0;

            if (s[8].Equals('P'))
            {
                timeFormat = 24;
                hour = Convert.ToInt32(s.Substring(0, 2));
                if (hour < 12)
                {
                    hour = (hour+12) % timeFormat;
                }
            }
            else
            {
                hour = (Convert.ToInt32(s.Substring(0, 2)) + 12) % timeFormat;
            }

            return hour.ToString().PadLeft(2,'0') + s.Substring(2, 6);
        }

        public static string TimeConversionV2(string s)
        {
            var hour = Convert.ToInt32(s.Substring(0,2)) % 12;
            
            if (s[8].Equals('P'))
            {
                hour += 12;
            }

            return string.Format("{0}{1}", hour.ToString().PadLeft(2, '0'), s.Substring(2, 6));
        }

        public static bool HasEnoughNoteLettersFromMagazine(string magazine, string note)
        {
            var magLetters = new Dictionary<char, int>();

            foreach (char c in magazine)
            {
                if (magLetters.ContainsKey(c))
                {
                    magLetters[c]++;
                }
                else
                {
                    magLetters.Add(c, 1);
                }
            }

            foreach (char noteL in note)
            {
                if (magLetters.ContainsKey(noteL))
                {
                    magLetters[noteL]--;
                    if (magLetters[noteL] < 0)
                    {
                        return false; //out of letters for note
                    }
                }
                else
                {
                    return false; // does not contain needed letter
                }
            }

            return true;
        }

    }
}
