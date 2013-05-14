{
  'targets': [
    {
      'target_name': 'binding',
      'include_dirs': ['/usr/local/include/lame', '/usr/local/include'],
      'libraries': ['-L/usr/local/lib -lmpg123'],
      'sources': [
        'src/binding.cc',
      ],
    }
  ]
}
