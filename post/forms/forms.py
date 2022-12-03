from django import forms
from django.forms import ImageField, TextInput, FileInput

from ..models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'thumbnail')
        #No logré poder estilar la etiqueta label de cada field.
        
        widgets = {
            'title': TextInput(attrs={'class': 'input is-primary m-5 input-label',
                                          'placeholder': 'e.g. Learn Python'}),
                                    

                      
            'content': TextInput(attrs={'class': 'textarea is-primary m-5 is-medium',
                                        'placeholder': 'type your content here'
                                        }),
            # 'summary': TextInput(attrs={'class': 'textarea is-primary m-5 is-medium',
            #                             'placeholder': 'type your summary here'
            #                             }),
            
        }



       