"""Tools for the slides_agent."""

# Slide creation and management: InsertNewSlides then ModifySlide
from .ApplyPptxTextReplacements import ApplyPptxTextReplacements

# PPTX building and validation
from .BuildPptxFromHtmlSlides import BuildPptxFromHtmlSlides
from .CheckSlide import CheckSlide
from .CheckSlideCanvasOverflow import CheckSlideCanvasOverflow
from .CreateImageMontage import CreateImageMontage
from .CreatePptxThumbnailGrid import CreatePptxThumbnailGrid
from .DeleteSlide import DeleteSlide
from .DownloadImage import DownloadImage

# Asset utilities
from .EnsureRasterImage import EnsureRasterImage

# Template-based editing (for existing PPTX files)
from .ExtractPptxTextInventory import ExtractPptxTextInventory
from .GenerateImage import GenerateImage
from .ImageSearch import ImageSearch
from .InsertNewSlides import InsertNewSlides
from .ManageTheme import ManageTheme
from .ModifySlide import ModifySlide
from .ReadSlide import ReadSlide
from .RearrangePptxSlidesFromTemplate import RearrangePptxSlidesFromTemplate
from .RestoreSnapshot import RestoreSnapshot
from .SlideScreenshot import SlideScreenshot

__all__ = [
    # Slide management
    "InsertNewSlides",
    "ModifySlide",
    "ManageTheme",
    "DeleteSlide",
    "SlideScreenshot",
    "ReadSlide",
    # PPTX building
    "BuildPptxFromHtmlSlides",
    "RestoreSnapshot",
    "CreatePptxThumbnailGrid",
    "CheckSlideCanvasOverflow",
    "CheckSlide",
    # Template editing
    "ExtractPptxTextInventory",
    "RearrangePptxSlidesFromTemplate",
    "ApplyPptxTextReplacements",
    # Assets
    "EnsureRasterImage",
    "CreateImageMontage",
    "DownloadImage",
    "ImageSearch",
    "GenerateImage",
]
