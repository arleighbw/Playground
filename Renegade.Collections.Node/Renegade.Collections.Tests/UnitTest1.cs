using System;
using Xunit;

namespace Renegade.Collections.Tests
{
    public class NodeTests
    {
        [Fact]
        public void SameString_NodeEquals_True()
        {
            Node<string> node = new Node<string>("blayne");
            Node<string> node2 = new Node<string>("blayne");

            var actual = node.Equals(node2);

            Assert.True(actual);
        }

        [Fact]
        public void DiffString_NodeEquals_False()
        {
            Node<string> node = new Node<string>("blayne");
            Node<string> node2 = new Node<string>("wilson");

            var actual = node.Equals(node2);

            Assert.False(actual);
        }

        [Fact]
        public void null_NodeEquals_False()
        {
            Node<string> node = new Node<string>("blayne");
            Node<string> node2 = null;

            var actual = node.Equals(node2);

            Assert.False(actual);
        }

        [Fact]
        public void emptyString_NodeEquals_False()
        {
            Node<string> node = new Node<string>("blayne");
            Node<string> node2 = new Node<string>(string.Empty);

            var actual = node.Equals(node2);

            Assert.False(actual);
        }

        [Fact]
        public void SameNode_NodeEqualEqual_False()
        {
            Node<string> node = new Node<string>("blayne");
            Node<string> node2 = new Node<string>("blayne");

            var actual = (node == node2);

            Assert.False(actual);
        }

        [Fact]
        public void SameNodeRef_RefNodeEqualEqualNode_True()
        {
            Node<string> node = new Node<string>("blayne");
            Node<string> root = node;

            var actual = (node == root);

            Assert.True(actual);
        }
    }
}
