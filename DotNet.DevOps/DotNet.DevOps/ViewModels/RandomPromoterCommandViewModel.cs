using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using DotNet.DevOps.Models;

namespace DotNet.DevOps.ViewModels
{
    public class RandomPromoterCommandViewModel
    {
        public PromoterCommands PromoterCommand { get; set; }
        public List<Developer> Developers { get; set; }
    }
}