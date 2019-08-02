public static class EnumUtil 
{
    //usage: var values = EnumUtil.GetValues<Foos>();
    public static IEnumerable<T> GetValues<T>() 
    {
        return Enum.GetValues(typeof(T)).Cast<T>();
    }
}
