from django.contrib import admin
from django.contrib import admin
from django.utils.html import format_html
from .models import Slide


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'shape_class', 'background_preview')
    search_fields = ('title', 'subtitle')
    list_filter = ('shape_class',)
    readonly_fields = ('background_preview', 'shape1_preview', 'shape2_preview', 'shape3_preview')

    fieldsets = (
        ("Basic Info", {
            'fields': ('title', 'subtitle', 'shape_class'),
        }),
        ("Background", {
            'fields': ('background_image', 'background_preview'),
            'description': (
                "<div style='padding:10px; background:#eef9ff; border:1px solid #cce7ff; "
                "border-radius:6px; margin:10px 0;'>"
                "<h4 style='margin-top:0; color:#0073e6;'>📐 Image Size Guide</h4>"
                "<ul style='margin:0; padding-left:20px; color:#004466;'>"
                "<li><b>Background Image:</b> 1920 × 1080 px (16:9 ratio)</li>"
                "</ul>"
                "</div>"
            )
        }),
        ("Shapes", {
            'fields': ('shape1', 'shape1_preview', 'shape2', 'shape2_preview', 'shape3', 'shape3_preview'),
            'description': (
                "<div style='padding:10px; background:#fef6e4; border:1px solid #fcd34d; "
                "border-radius:6px; margin:10px 0;'>"
                "<h4 style='margin-top:0; color:#b45309;'>🎨 Shape Images</h4>"
                "<ul style='margin:0; padding-left:20px; color:#78350f;'>"
                "<li><b>Shape Images:</b> 300 × 300 px (square, transparent PNG preferred)</li>"
                "</ul>"
                "</div>"
            )
        }),
    )

    # -------- Image Preview Methods --------
    def background_preview(self, obj):
        if obj.background_image:
            return format_html('<img src="{}" width="200" style="border-radius:8px; border:2px solid #ddd;"/>', obj.background_image.url)
        return "—"
    background_preview.short_description = "Background Preview"

    def shape1_preview(self, obj):
        if obj.shape1:
            return format_html('<img src="{}" width="80" style="border-radius:6px; border:1px solid #ddd;"/>', obj.shape1.url)
        return "—"
    shape1_preview.short_description = "Shape 1 Preview"

    def shape2_preview(self, obj):
        if obj.shape2:
            return format_html('<img src="{}" width="80" style="border-radius:6px; border:1px solid #ddd;"/>', obj.shape2.url)
        return "—"
    shape2_preview.short_description = "Shape 2 Preview"

    def shape3_preview(self, obj):
        if obj.shape3:
            return format_html('<img src="{}" width="80" style="border-radius:6px; border:1px solid #ddd;"/>', obj.shape3.url)
        return "—"
    shape3_preview.short_description = "Shape 3 Preview"



from django.contrib import admin
from django.utils.html import format_html
from .models import ProductCollection, ProductCard, ProductCatalogue, CatalogueCard


# ------------------ ProductCollection ------------------
class ProductCardInline(admin.TabularInline):
    model = ProductCard
    extra = 1
    fields = ('preview', 'image', 'color', 'size')
    readonly_fields = ('preview',)
    verbose_name = "Product Card"
    verbose_name_plural = "Product Cards"

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:6px;"/>', obj.image.url)
        return "—"
    preview.short_description = "Preview"

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.base_fields['image'].help_text = (
            "📐 Recommended size: 500 × 400 px (card image)"
        )
        return formset


@admin.register(ProductCollection)
class ProductCollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'main_image_preview')
    inlines = [ProductCardInline]

    fieldsets = (
        ("Basic Info", {
            'fields': ('title', 'subtitle'),
        }),
        ("Main Image", {
            'fields': ('main_image', 'main_image_preview'),
            'description': (
                "<div style='padding:10px; background:#eef9ff; border:1px solid #cce7ff; "
                "border-radius:6px; margin:10px 0;'>"
                "<h4 style='margin-top:0; color:#0073e6;'>📐 Image Size Guide</h4>"
                "<ul style='margin:0; padding-left:20px; color:#004466;'>"
                "<li><b>Main Product Image:</b> 1600 × 900 px (16:9 ratio, large background)</li>"
                "<li><b>Card Images:</b> 500 × 400 px (for product details)</li>"
                "</ul>"
                "</div>"
            )
        }),
    )

    readonly_fields = ('main_image_preview',)

    def main_image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="200" style="border:2px solid #ddd; border-radius:8px;"/>', obj.main_image.url)
        return "—"
    main_image_preview.short_description = "Main Image Preview"


# ------------------ ProductCatalogue ------------------
class CatalogueCardInline(admin.TabularInline):
    model = CatalogueCard
    extra = 1
    fields = ('preview', 'image', 'color', 'size')
    readonly_fields = ('preview',)
    verbose_name = "Catalogue Card"
    verbose_name_plural = "Catalogue Cards"

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="border-radius:6px;"/>', obj.image.url)
        return "—"
    preview.short_description = "Preview"

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.base_fields['image'].help_text = (
            "📐 Recommended size: 500 × 400 px (card image)"
        )
        return formset


@admin.register(ProductCatalogue)
class ProductCatalogueAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'main_image_preview')
    search_fields = ('title', 'subtitle')
    inlines = [CatalogueCardInline]

    fieldsets = (
        ("Basic Info", {
            'fields': ('title', 'subtitle'),
        }),
        ("Main Image", {
            'fields': ('main_image', 'main_image_preview'),
            'description': (
                "<div style='padding:10px; background:#eef9ff; border:1px solid #cce7ff; "
                "border-radius:6px; margin:10px 0;'>"
                "<h4 style='margin-top:0; color:#0073e6;'>📐 Image Size Guide</h4>"
                "<ul style='margin:0; padding-left:20px; color:#004466;'>"
                "<li><b>Main Catalogue Image:</b> 1600 × 900 px (16:9 ratio, large background)</li>"
                "<li><b>Card Images:</b> 500 × 400 px (for catalogue details)</li>"
                "</ul>"
                "</div>"
            )
        }),
    )

    readonly_fields = ('main_image_preview',)

    def main_image_preview(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="200" style="border:2px solid #ddd; border-radius:8px;"/>', obj.main_image.url)
        return "—"
    main_image_preview.short_description = "Main Image Preview"

from django.contrib import admin
from .models import ProductEnquiry

admin.site.register(ProductEnquiry)






from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1 # default two extra image fields in admin

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)


from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
