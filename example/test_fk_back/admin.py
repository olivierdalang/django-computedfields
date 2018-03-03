# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import NormalModel, Foo, Bar, Baz


class TestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'baz_names'
    )


admin.site.register(NormalModel, TestAdmin)


class FooAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'baz_names'
    )


admin.site.register(Foo, FooAdmin)


class BarAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'baz_names'
    )


admin.site.register(Bar, BarAdmin)


class BazAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Baz, BazAdmin)