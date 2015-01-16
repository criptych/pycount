"""These are all the patterns used by pycount, in one place, separated from
   the code.
"""

FILE_TYPE_PATTERNS = {
    '.abap': 'ABAP',
    '.ac': 'm4',
    '.ada': 'Ada',
    '.adb': 'Ada',
    '.ads': 'Ada',
    '.adso': 'ADSO/IDSM',
    '.ahk': 'AutoHotkey',
    '.ample': 'AMPLE',
    '.as': 'ActionScript',
    '.dofile': 'AMPLE',
    '.startup': 'AMPLE',
    '.asa': 'ASP',
    '.asax': 'ASP.Net',
    '.ascx': 'ASP.Net',
    '.asm': 'Assembly',
    '.asmx': 'ASP.Net',
    '.asp': 'ASP',
    '.aspx': 'ASP.Net',
    '.master': 'ASP.Net',
    '.sitemap': 'ASP.Net',
    '.cshtml': 'Razor',
    '.bas': 'Visual Basic',
    '.bat': 'DOS Batch',
    '.BAT': 'DOS Batch',
    '.build.xml': 'Ant',
    '.cbl': 'COBOL',
    '.CBL': 'COBOL',
    '.c': 'C',
    '.C': 'C++',
    '.cc': 'C++',
    '.c++': 'C++',
    '.ccs': 'CCS',
    '.cfc': 'ColdFusion CFScript',
    '.cfm': 'ColdFusion',
    '.cl': 'Lisp/OpenCL',
    '.clj': 'Clojure',
    '.cljs': 'ClojureScript',
    '.cls': 'Visual Basic',
    '.cmake': 'CMake',
    '.cob': 'COBOL',
    '.COB': 'COBOL',
    '.coffee': 'CoffeeScript',
    '.component': 'Visualforce Component',
    '.config': 'ASP.Net',
    '.cpp': 'C++',
    '.cs': 'C#',
    '.css': "CSS",
    '.ctl': 'Visual Basic',
    '.cxx': 'C++',
    '.d': 'D',
    '.da': 'DAL',
    '.dart': 'Dart',
    '.def': 'Teamcenter def',
    '.dmap': 'NASTRAN DMAP',
    '.dpr': 'Pascal',
    '.dsr': 'Visual Basic',
    '.dtd': 'DTD',
    '.ec': 'C',
    '.el': 'Lisp',
    '.erl': 'Erlang',
    '.exp': 'Expect',
    '.f77': 'Fortran 77',
    '.F77': 'Fortran 77',
    '.f90': 'Fortran 90',
    '.F90': 'Fortran 90',
    '.f95': 'Fortran 95',
    '.F95': 'Fortran 95',
    '.f': 'Fortran 77',
    '.F': 'Fortran 77',
    '.fmt': 'Oracle Forms',
    '.focexec': 'Focus',
    '.frm': 'Visual Basic',
    '.gnumakefile': 'make',
    '.Gnumakefile': 'make',
    '.go': 'Go',
    '.groovy': 'Groovy',
    '.gant': 'Groovy',
    '.h': 'C/C++ Header',
    '.H': 'C/C++ Header',
    '.hh': 'C/C++ Header',
    '.hpp': 'C/C++ Header',
    '.hrl': 'Erlang',
    '.hs': 'Haskell',
    '.htm': 'HTML',
    '.html': 'HTML',
    '.i3': 'Modula3',
    '.ism': 'InstallShield',
    '.pro': 'IDL',
    '.ig': 'Modula3',
    '.il': 'SKILL',
    '.ils': 'SKILL++',
    '.inc': 'PHP/Pascal',
    '.ino': 'Arduino Sketch',
    '.pde': 'Arduino Sketch',
    '.itk': 'Tcl/Tk',
    '.java': 'Java',
    '.jcl': 'JCL',
    '.jl': 'Lisp',
    '.js': 'Javascript',
    '.jsf': 'JavaServer Faces',
    '.json': 'JSON',
    '.xhtml': 'JavaServer Faces',
    '.jsp': 'JSP',
    '.ksc': 'Kermit',
    '.lhs': 'Haskell',
    '.l': 'lex',
    '.less': 'LESS',
    '.lsp': 'Lisp',
    '.lisp': 'Lisp',
    '.m3': 'Modula3',
    '.m4': 'm4',
    '.met': 'Teamcenter met',
    '.wdproj': 'MSBuild script',
    '.vcproj': 'MSBuild script',
    '.wixproj': 'MSBuild script',
    '.vbproj': 'MSBuild script',
    '.csproj': 'MSBuild script',
    '.mg': 'Modula3',
    '.ml': 'OCaml',
    '.mli': 'OCaml',
    '.mly': 'OCaml',
    '.mll': 'OCaml',
    '.m': 'MATLAB/Objective C/MUMPS',
    '.mm': 'Objective C++',
    '.mps': 'MUMPS',
    '.mth': 'Teamcenter mth',
    '.oscript': 'LiveLink OScript',
    '.pad': 'Ada',
    '.page': 'Visualforce Page',
    '.pas': 'Pascal',
    '.pcc': 'C++',
    '.pfo': 'Fortran 77',
    '.pgc': 'C',
    '.php3': 'PHP',
    '.php4': 'PHP',
    '.php5': 'PHP',
    '.php': 'PHP',
    '.pig': 'Pig Latin',
    '.plh': 'Perl',
    '.pl': 'Perl',
    '.PL': 'Perl',
    '.plx': 'Perl',
    '.pm': 'Perl',
    '.pom.xml': 'Maven',
    '.pom': 'Maven',
    '.p': 'Pascal',
    '.pp': 'Pascal',
    '.psql': 'SQL',
    '.py': 'Python',
    '.pyx': 'Cython',
    '.qml': 'QML',
    '.rb': 'Ruby',
    '.rex': 'Oracle Reports',
    '.rexx': 'Rexx',
    '.rhtml': 'Ruby HTML',
    '.rs': 'Rust',
    '.s': 'Assembly',
    '.S': 'Assembly',
    '.scala': 'Scala',
    '.sbl': 'Softbridge Basic',
    '.SBL': 'Softbridge Basic',
    '.sc': 'Lisp',
    '.scm': 'Lisp',
    '.ses': 'Patran Command Language',
    '.pcl': 'Patran Command Language',
    '.ps1': 'PowerShell',
    '.sass': 'SASS',
    '.scss': 'SASS',
    '.smarty': 'Smarty',
    '.sql': 'SQL',
    '.SQL': 'SQL',
    '.sproc.sql': 'SQL Stored Procedure',
    '.spoc.sql': 'SQL Stored Procedure',
    '.spc.sql': 'SQL Stored Procedure',
    '.udf.sql': 'SQL Stored Procedure',
    '.data.sql': 'SQL Data',
    '.v': 'Verilog-SystemVerilog',
    '.sv': 'Verilog-SystemVerilog',
    '.svh': 'Verilog-SystemVerilog',
    '.tk': 'Tcl/Tk',
    '.tpl': 'Smarty',
    '.trigger': 'Apex Trigger',
    '.vala': 'Vala',
    '.vapi': 'Vala Header',
    '.vhd': 'VHDL',
    '.VHD': 'VHDL',
    '.vhdl': 'VHDL',
    '.VHDL': 'VHDL',
    '.vba': 'Visual Basic',
    '.VBA': 'Visual Basic',
    '.vb': 'Visual Basic',
    '.VB': 'Visual Basic',
    '.vbs': 'Visual Basic',
    '.VBS': 'Visual Basic',
    '.webinfo': 'ASP.Net',
    '.xml': 'XML',
    '.XML': 'XML',
    '.mxml': 'MXML',
    '.build': 'NAnt scripts',
    '.vim': 'vim script',
    '.xaml': 'XAML',
    '.xsd': 'XSD',
    '.XSD': 'XSD',
    '.xslt': 'XSLT',
    '.XSLT': 'XSLT',
    '.xsl': 'XSLT',
    '.XSL': 'XSLT',
    '.y': 'yacc',
    '.yaml': 'YAML',
    '.yml': 'YAML',
    '.awk': 'awk',
    '.bash': 'Bourne Again Shell',
    '.bc': 'bc',
    '.csh': 'C Shell',
    '.dmd': 'D',
    '.idl': 'IDL',
    '.kermit': 'Kermit',
    '.ksh': 'Korn Shell',
    '.lua': 'Lua',
    '.octave': 'Octave',
    '.perl5': 'Perl',
    '.perl': 'Perl',
    '.ruby': 'Ruby',
    '.sed': 'sed',
    '.sh': 'Bourne Shell',
    '.tcl': 'Tcl/Tk',
    '.tclsh': 'Tcl/Tk',
    '.tcsh': 'C Shell',
    '.wish': 'Tcl/Tk'
}

COMMENT_PATTERNS = {
}


BY_FILES_PATTERNS = {
    'Makefile': 'make',
    'makefile': 'make',
    'gnumakefile': 'make',
    'Gnumakefile': 'make',
    'CMakeLists.txt': 'CMake',
    'build.xml': 'Ant/XML',
    'pom.xml': 'Maven/XML',
    'Rakefile': 'Ruby',
    'rakefile': 'Ruby'
}

IGNORE_PATTERNS = ['.git', '.hg', '.svn']