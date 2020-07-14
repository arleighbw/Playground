using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using DotNet.DevOps.Models;
using DotNet.DevOps.ViewModels;

namespace DotNet.DevOps.Controllers
{
    public class PromoterCommandsController : Controller
    {
        // GET: PromoterCommands/Random
        public ActionResult Random()
        {
            var promCmd = new PromoterCommands() { Name = "BACKUPDAT"};
            var developers = new List<Developer>
            {
                new Developer() { Name = "B1" },
                new Developer() { Name = "B2" }
            };

            var viewModel = new RandomPromoterCommandViewModel
            {
                PromoterCommand = promCmd,
                Developers = developers
            };

            return View(viewModel);
        }

        [Route("promotercommands/released/{commit:regex(\\d{4}:range(1:10))}")]
        public ActionResult ByCommit(int commit)
        {
            return Content($"commit : {commit.ToString()}");
        }
    }
}