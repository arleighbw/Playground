using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq.Expressions;
using System.Security.AccessControl;
using MoreLinq;
using static System.Console;

/// <summary>
/// For my reference
/// From Design Patterns in C# and .Net, Dmitri Nesteruk
/// 
/// Commented Sections below Uses reflection to get around open-closed Principle
/// 
/// </summary>
namespace Renegade.DesignPatterns.Structural
{
    /// <summary>
    /// Adapter - Construct which adapts an existing interface X to conform to the required interface Y
    /// </summary>
    /// 

    public class Point
    {
        public int X;
        public int Y;

        public Point(int x, int y)
        {
            this.X = x;
            this.Y = y;
        }

        public override string ToString()
        {
            return $"{nameof(X)}: {X}, {nameof(Y)}: {Y}";
        }
    }

    public class Line
    {
        public Point Start, End;

        public Line(Point start, Point end)
        {
            if (start == null)
            {
                throw new ArgumentNullException(paramName: nameof(start));
            }
            if (end == null)
            {
                throw new ArgumentNullException(paramName: nameof(end));
            }
            this.Start = start;
            this.End = end;
        }
    }

    public class VectorObject : Collection<Line>
    {

    }

    public class VectorRectangle : VectorObject
    {
        public VectorRectangle(int x, int y, int width, int height)
        {
            Add(new Line(new Point(x, y), new Point(x + width, y)));
            Add(new Line(new Point(x + width, y), new Point(x + width, y + height)));
            Add(new Line(new Point(x, y), new Point(x, y + height)));
            Add(new Line(new Point(x, y + height), new Point(x + width, y + height)));
        }
    }

    public class LineToPointAdapter : Collection<Point>
    {
        private static int count = 0;

        public LineToPointAdapter(Line line)
        {
            WriteLine($"{++count}: Generating points for line [{line.Start.X},{line.Start.Y}]-[{line.End.X},{line.End.Y}] (no caching)");

            int left = Math.Min(line.Start.X, line.End.X);
            int right = Math.Max(line.Start.X, line.End.X);
            int top = Math.Min(line.Start.Y, line.End.Y);
            int bottom = Math.Max(line.Start.Y, line.End.Y);
            int dx = right - left;
            int dy = line.End.Y - line.Start.Y;

            if (dx == 0)
            {
                for (int y = top; y <= bottom; ++y)
                {
                    Add(new Point(left, y));
                }
            }
            else if (dy == 0)
            {
                for (int x = left; x <= right; ++x)
                {
                    Add(new Point(x, top));
                }
            }
        }
    }

    public class Demo
    {
        private static readonly List<VectorObject> _vectorObjects = new List<VectorObject>()
        {
          new VectorRectangle(1, 1, 10, 10),
          new VectorRectangle(3, 3, 6, 6)
        };

        // the interface we have
        public static void DrawPoint(Point p)
        {
            Write(".");
        }

        static void Main()
        {
            Draw();
            Draw();
        }

        private static void Draw()
        {
            foreach (var vo in _vectorObjects)
            {
                foreach (var line in vo)
                {
                    var adapter = new LineToPointAdapter(line);
                    adapter.ForEach(DrawPoint);
                }
            }
        }
    }
}
