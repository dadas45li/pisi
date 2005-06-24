<?xml version="1.0" encoding="utf-8" standalone="no"?>

<!DOCTYPE PSPEC SYSTEM
	  "http://www.uludag.org.tr/projeler/pisi/pisi-spec.dtd">

<PISI>

  <Source>
    <Name>startup-notification</Name>
    <Homepage>http://www.freedesktop.org/software/startup-notification/</Homepage>
    <Packager>
      <Name>Kirmizi kafalar</Name>
      <Email>hotmail@redhat.com</Email>
    </Packager>
    <License>LGPL-2, BSD</License>
    <IsA>library:x11</IsA>
    <PartOf>rpm:archive</PartOf>
    <Description>Application startup notification and feedback library</Description>
    <Archive archType="tarbz2" sha1sum="d2b5698b6209b5172d17222a3117db6447d7cdf1">
        ftp://ftp.linux.org.tr/pub/mirrors/gentoo/distfiles/startup-notification-0.8.tar.bz2
    </Archive>
    <BuildDependencies>
      <Dependency versionFrom="1.8"> make </Dependency>
    </BuildDependencies>
    <History>
      <Update>
	<Date>06/24/2005</Date>
	<Version>0.8</Version>
	<Release>2</Release>
      </Update>
      <Update>
	<Date>06/10/2005</Date>
	<Version>0.7</Version>
	<Release>2</Release>
      </Update>
    </History>
  </Source>

  <Package>
    <Name>startup-notification</Name>
    <Summary xml:lang="en">Application startup notification and feedback library</Summary>
    <Description>library files for startup-notification</Description>
    <Files>
      <Path fileType="sharedLib">/usr/lib</Path>
      <Path fileType="doc">/usr/share/doc</Path>
      <Path fileType="header">/usr/include</Path>
    </Files>
    <History>
      <Update>
	<Date>06/24/2005</Date>
	<Version>0.8</Version>
	<Release>2</Release>
      </Update>
    </History>
  </Package>
</PISI>
