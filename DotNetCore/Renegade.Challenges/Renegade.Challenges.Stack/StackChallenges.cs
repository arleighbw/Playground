using System;
using System.Collections.Generic;

namespace Renegade.Challenges.Stack
{
    public class StackChallenges
    {
        public static bool IsBalancedBracket(string s)
        {
            var stack = new Stack<char>();

            foreach (var bracket in s)
            {
                if (bracket.Equals('{')) stack.Push('}');
                else if (bracket.Equals('[')) stack.Push(']');
                else if (bracket.Equals('(')) stack.Push(')');
                else
                {
                    if (stack.Count == 0 || !stack.Pop().Equals(bracket)) return false;
                }
            }

            return true;
        }
    }
}
