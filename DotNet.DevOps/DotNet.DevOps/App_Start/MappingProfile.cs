using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using AutoMapper;
using DotNet.DevOps.Dtos;
using DotNet.DevOps.Models;

namespace DotNet.DevOps.App_Start
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            Mapper.CreateMap<Developer, DeveloperDto>();
            Mapper.CreateMap<DeveloperDto, Developer>();
        }
    }
}