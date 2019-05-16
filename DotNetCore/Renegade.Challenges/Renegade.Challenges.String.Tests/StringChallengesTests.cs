using System;
using Xunit;

namespace Renegade.Challenges
{
    /// <summary>
    /// CountMessageInterference Tests
    /// </summary>
    public class StringChallengesTests_CountMessageInterference
    {
        [Fact]
        public void SOS_CountMessageInterference_Pass()
        {
            var actual = String.StringChallenges.CountMessageInterference("SOSSPSSQSSOR", "SOS");

            Assert.Equal(3, actual);
        }

    }

    /// <summary>
    /// StringChallengesTests_RepeatedString Tests
    /// </summary>
    public class StringChallengesTests_RepeatedString
    {
        [Fact]
        public void LargeAAB_RepeatedStringSearchOccurences_588525()
        {
            var s = "aab";
            var n = 882787;

            var actual = String.StringChallenges.RepeatedStringSearchOccurences(s, n);

            Assert.Equal(588525, actual);
        }

        [Fact]
        public void Large_RepeatedStringSearchOccurences_588525()
        {
            var s = "aab";
            var n = 882787;

            var actual = String.StringChallenges.RepeatedStringSearchOccurences(s, n);

            Assert.Equal(588525, actual);
        }

        [Fact]
        public void Small_RepeatedStringSearchOccurences_1000000000000()
        {
            var s = "a";
            var n = 1000000000000;

            var actual = String.StringChallenges.RepeatedStringSearchOccurences(s, n);

            Assert.Equal(1000000000000, actual);
        }

        
        [Fact]
        public void Large_RepeatedStringSearchOccurences_515745234480()
        {
            var s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm";
            var n = 736778906400;

            var actual = String.StringChallenges.RepeatedStringSearchOccurences(s, n);

            Assert.Equal(51574523448, actual);
        }
    }

    /// <summary>
    /// TimeConversion Tests
    /// </summary>
    public class StringChallengesTests_TimeConversion
    {
        [Fact]
        public void AMTwelve_TimeConversion_Pass()
        {
            var time = "12:40:22AM";
            var actual = String.StringChallenges.TimeConversion(time);

            Assert.Equal("00:40:22", actual);
        }

        [Fact]
        public void AMSix_TimeConversion_Pass()
        {
            var time = "06:40:03AM";
            var actual = String.StringChallenges.TimeConversion(time);

            Assert.Equal("06:40:03", actual);
        }

        [Fact]
        public void PMSeven_TimeConversion_Pass()
        {
            var time = "07:05:45PM";
            var actual = String.StringChallenges.TimeConversion(time);

            Assert.Equal("19:05:45", actual);
        }

        [Fact]
        public void PMTwelve_TimeConversion_Pass()
        {
            var time = "12:45:54PM";
            var actual = String.StringChallenges.TimeConversion(time);

            Assert.Equal("12:45:54", actual);
        }
    }

    /// <summary>
    /// TimeConversion Tests
    /// </summary>
    public class StringChallengesTests_TimeConversionV2
    {
        [Fact]
        public void AMTwelve_TimeConversionV2_Pass()
        {
            var time = "12:40:22AM";
            var actual = String.StringChallenges.TimeConversionV2(time);

            Assert.Equal("00:40:22", actual);
        }

        [Fact]
        public void AMSix_TimeConversionV2_Pass()
        {
            var time = "06:40:03AM";
            var actual = String.StringChallenges.TimeConversionV2(time);

            Assert.Equal("06:40:03", actual);
        }

        [Fact]
        public void PMSeven_TimeConversionV2_Pass()
        {
            var time = "07:05:45PM";
            var actual = String.StringChallenges.TimeConversionV2(time);

            Assert.Equal("19:05:45", actual);
        }

        [Fact]
        public void PMTwelve_TimeConversionV2_Pass()
        {
            var time = "12:45:54PM";
            var actual = String.StringChallenges.TimeConversionV2(time);

            Assert.Equal("12:45:54", actual);
        }
    }

    public class StringChallengesTests_HasEnoughNoteLettersFromMagazine
    {
        [Fact]
        public void HasNoteLetters_HasEnoughNoteLettersFromMagazine_True()
        {
            var magazine = "zahk dp apdz clo e dk awfvf osb qr sa cqjq zgr nvxtb abjy axa ili wdyw soqku buwcl qcub sautu ii vkrzl bdob nona al zg ombzc c dbun f xkuo lsax hfki j dfft uce ugj ywz vucgg xq udrkt ypy tmxgc ty gar kty dc bznj pzzx clo apdz nvxtb clo sa clo zahk awfvf soqku udrkt udrkt e ypy xkuo tmxgc ombzc wdyw al axa lsax clo abjy osb apdz bdob pzzx zahk c bznj gar osb xkuo zahk zg uce zg clo e apdz gar xq dbun buwcl ili bznj clo osb dc dbun ywz";
            var note = "buwcl qr axa ypy zahk nvxtb dp hfki ii uce dc zg dbun ypy ty cqjq zg kty bznj zg zahk dp c al ugj ywz qcub ywz wdyw hfki gar e axa dp qr kty bznj clo ty vucgg qcub al vkrzl qcub j awfvf soqku lsax bdob nvxtb";

            var actual = String.StringChallenges.HasEnoughNoteLettersFromMagazine(magazine, note);

            Assert.True(actual);
        }

        [Fact]
        public void HasNoteLettersShort_HasEnoughNoteLettersFromMagazine_True()
        {
            var magazine = "bbllaayynnee";
            var note = "blayne";

            var actual = String.StringChallenges.HasEnoughNoteLettersFromMagazine(magazine, note);

            Assert.True(actual);
        }
    }


}
