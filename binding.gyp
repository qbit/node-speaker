{
  'targets': [
    {
      'target_name': 'binding',
      'include_dirs': [
	      '/usr/local/include/lame', 
	      '/usr/local/include',
	      './deps/mpg123/src/output'
      ],
      'libraries': ['-L/usr/local/lib -lmpg123'],
      'sources': [
        'src/binding.cc',
      ],
    }
  ]
}
