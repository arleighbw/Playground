using System;
using Xunit;

namespace Renegade.Collections.Problems
{
    public class SinglyLinkedList_Problem_ChallengeTests
    {

        [Fact]
        public void OddList_GetMiddleNodeSinglyLinkedList_Pass()
        {
            var linkedList = new SinglyLinkedList_Problem<int>();
            linkedList.Add(1);
            linkedList.Add(2);
            linkedList.Add(3);
            linkedList.Add(4);
            linkedList.Add(5);

            var actual = linkedList.GetMiddleNode();

            Assert.Equal(3, actual);
        }

        [Fact]
        public void EvenList_GetMiddleNodeSinglyLinkedList_Pass()
        {
            var linkedList = new SinglyLinkedList_Problem<int>();
            linkedList.Add(1);
            linkedList.Add(2);
            linkedList.Add(3);
            linkedList.Add(4);
            linkedList.Add(5);
            linkedList.Add(6);

            var actual = linkedList.GetMiddleNode();

            Assert.Equal(4, actual);
        }

        [Fact]
        public void EmptyList_GetMiddleNodeSinglyLinkedList_Pass()
        {
            var linkedList = new SinglyLinkedList_Problem<int>();

            var actual = linkedList.GetMiddleNode();

            Assert.Equal(0, actual);
        }

        [Fact]
        public void StringPalindrome_IsPalindromeUsingStack_Pass()
        {
            var linkedList = new SinglyLinkedList_Problem<char>();
            linkedList.Add('r');
            linkedList.Add('a');
            linkedList.Add('d');
            linkedList.Add('a');
            linkedList.Add('r');

            var actual = linkedList.IsPalindromeUsingStack();

            Assert.True(actual);
        }

        [Fact]
        public void StringFalsePalindrome_IsPalindromeUsingStack_Pass()
        {
            var linkedList = new SinglyLinkedList_Problem<char>();
            linkedList.Add('b');
            linkedList.Add('l');
            linkedList.Add('a');
            linkedList.Add('y');
            linkedList.Add('n');
            linkedList.Add('e');

            var actual = linkedList.IsPalindromeUsingStack();

            Assert.False(actual);
        }
    }
}
