using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Linq;
using System.Net;
using System.Web.Http;
using AutoMapper;
using DotNet.DevOps.Dtos;
using DotNet.DevOps.Models;

namespace DotNet.DevOps.Controllers.API
{
    public class DevelopersController : ApiController
    {
        private List<Developer> _Developers { get; set; }

        public DevelopersController()
        {
            _Developers = new List<Developer>()
            {
                new Developer() { Id = 1, Name = "B1" },
                new Developer() { Id = 2, Name = "C1" }
            };

        }

        // GET /api/developers
        public IEnumerable<DeveloperDto> GetDevelopers()
        {
            return _Developers.Select(Mapper.Map<Developer, DeveloperDto>); 
        }

        // Get /api/developers/1
        public IHttpActionResult GetDeveloper(int id)
        {
            var developer = _Developers.SingleOrDefault(d => d.Id == id);

            if (developer == null)
                return NotFound();

            return Ok(Mapper.Map<Developer, DeveloperDto>(developer));
        }

        // POST /api/developers
        [HttpPost] // use? or not?
        public IHttpActionResult CreateDeveloper(DeveloperDto developerDto)
        {
            if (!ModelState.IsValid)
                return BadRequest();

            var developer = Mapper.Map<DeveloperDto, Developer>(developerDto);
            _Developers.Add(developer);

            return Created(new Uri(string.Concat(Request.RequestUri, developer.Id)), developerDto);
        }

        // PUT /api/developer/1
        [HttpPut]
        public void UpdateDeveloper(int id, DeveloperDto developerDto)
        {
            //TODO update to use IHttpActioNResult
            if (!ModelState.IsValid)
                throw new HttpResponseException(HttpStatusCode.BadRequest);

            var existingIndex = -1;
            for (var i = 0; i < _Developers.Count; i++)
            {
                if (_Developers[i].Id == id) existingIndex = i;
            }

            if (existingIndex < 0)
                throw new HttpResponseException(HttpStatusCode.NotFound);

            Mapper.Map(developerDto, _Developers[existingIndex]);
        }

        // DELETE /api/developers/1
        [HttpDelete]
        public void DeleteDeveloper(int id)
        {
            //TODO update to use IHttpActioNResult
            if (!ModelState.IsValid)
                throw new HttpResponseException(HttpStatusCode.BadRequest);

            var existingIndex = -1;
            for (var i = 0; i < _Developers.Count; i++)
            {
                if (_Developers[i].Id == id) existingIndex = i;
            }

            if (existingIndex < 0)
                throw new HttpResponseException(HttpStatusCode.NotFound);

            _Developers.RemoveAt(existingIndex);
        }
    }
}
