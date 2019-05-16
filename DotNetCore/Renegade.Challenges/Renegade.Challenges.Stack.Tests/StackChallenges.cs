using System;
using Xunit;

namespace Renegade.Challenges.Stack.Tests
{
    public class StackChallenges
    {
        [Fact]
        public void Balanced_IsBalancedBracket_True()
        {
            var s = "{{{[({()[][][][](){{}}})]}}}";

            var actual = Stack.StackChallenges.IsBalancedBracket(s);

            Assert.True(actual);
        }

        [Fact]
        public void NotBalanced_IsBalancedBracket_False()
        {
            var s = "{{]]{{]]";

            var actual = Stack.StackChallenges.IsBalancedBracket(s);

            Assert.False(actual);
        }
    }
}
