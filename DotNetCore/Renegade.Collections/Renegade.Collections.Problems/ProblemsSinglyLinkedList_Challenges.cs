using System;
using Xunit;

namespace Renegade.Collections.Problems
{
    public class ProblemsSinglyLinkedList_Challenges
    {

        [Fact]
        public void OddList_GetMiddleNodeSinglyLinkedList_Pass()
        {
            var linkedList = new ProblemSinglyLinkedList<int>();
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
            var linkedList = new ProblemSinglyLinkedList<int>();
            linkedList.Add(1);
            linkedList.Add(2);
            linkedList.Add(3);
            linkedList.Add(4);
            linkedList.Add(5);
            linkedList.Add(6);

            var actual = linkedList.GetMiddleNode();

            Assert.Equal(4, actual);
        }
    }
}
