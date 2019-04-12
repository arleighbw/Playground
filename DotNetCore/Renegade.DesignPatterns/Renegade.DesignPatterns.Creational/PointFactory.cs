using System;

/// <summary>
/// For my reference
/// From Design Patterns in C# and .Net, Dmitri Nesteruk
/// </summary>
namespace Renegade.DesignPatterns.Creational
{
    //Factory A component responsible solely for the wholesale (not piecewise) creation of objects

    //Separate component that knows how to initiliaze in a particular way.
    public static class PointFactory
    {
        public static Point NewCartesianPoint(double x, double y)
        {
            return new Point(x, y);
        }

        public static Point NewPolarPoint(double rho, double theta)
        {
            return new Point(rho * Math.Cos(theta), rho * Math.Sin(theta));
        }
    }

    public class Point
    {
        // factory method within class
        public static Point NewCartesianPoint(double x, double y)
        {
            return new Point(x, y);
        }

        public static Point NewPolarPoint(double rho, double theta)
        {
            return new Point(rho * Math.Cos(theta), rho * Math.Sin(theta));
        }

        private double X, Y;

        internal Point(double x, double y)
        {
            this.X = x;
            this.Y = y;
        }

        public override string ToString()
        {
            return $"{nameof(X)}: {X}, {nameof(Y)}: {Y}";
        }


        //Inner Factory
        //Can be static class
        //public static class Factory
        //{
        //    public static Point NewCartesianPoint(double x, double y)
        //    {
        //        return new Point(x, y);
        //    }

        //    public static Point NewPolarPoint(double rho, double theta)
        //    {
        //        return new Point(rho * Math.Cos(theta), rho * Math.Sin(theta));
        //    }
        //}


        //=> makes it a property, instanciates object
        public static Point Origin => new Point(0, 0);
        //Field init onces, BETTER !! Getter without Setter
        public static Point Origin2 = new Point(0, 0);

        //or you can use a property like below.. will instanciate object everytime
        //public static PointFactory Factory => new PointFactory();

        //You can use a property with getter only. Only instanciates once.
        public static PointFactory Factory = new PointFactory();

        public class PointFactory
        {
            public Point NewCartesianPoint(double x, double y)
            {
                return new Point(x, y);
            }

            public Point NewPolarPoint(double rho, double theta)
            {
                return new Point(rho * Math.Cos(theta), rho * Math.Sin(theta));
            }
        }
    }
}
