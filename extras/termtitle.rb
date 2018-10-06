class Termtitle < Formula
  homepage ""
  url "https://github.com/grimmer0125/terminal-title-change/archive/v0.1.8.tar.gz"
  sha256 "0c8f60819b7caa7f6bc087534cdbbfa814ba89e0658b53a65dc5bc2d6cd0d99f"

  def install    
    # 1. without this. 
    # no termtitle/0.1.7/bin folder and termtitle/libexec/bin are libexec/lib are empty
    system "python", *Language::Python.setup_install_args(libexec)    
    
    # 2. create a termtitle/0.1.7/bin/termtitle 
    # It is the executed file of the installed command, `termtitle new_title` 
    bin.install Dir["#{libexec}/bin/*"]  
    
    ENV.prepend_create_path "PYTHONPATH", libexec/"lib/python2.7/site-packages"  
    # 3. without this,
    # a. termtitle/0.1.7/libexec/bin/ <-become empty 
    # b. termtitle/0.1.7/bin/termtitle's content becomes original libexec/bin,
    # execute termtile, error: 
    # pkg_resources.DistributionNotFound: The 'termtitle==0.1.7' distribution was not found and is required by the application
    bin.env_script_all_files(libexec/"bin", :PYTHONPATH => ENV["PYTHONPATH"]) 

    # after brew install termtitle, 
    # file contents in /usr/local/Cellar/
    # a. termtitle/0.1.7/bin/termtitle:
    # PYTHONPATH="/usr/local/Cellar/termtitle/0.1.7/libexec/lib/python2.7/site-packages" exec "/usr/local/Cellar/termtitle/0.1.7/libexec/bin/termtitle" "$@"
    # b. termtitle/0.1.7/libexec/bin/termtitle:
    # __requires__ = 'termtitle==0.1.7'
    # import sys
    # from pkg_resources import load_entry_point
    # if __name__ == '__main__':
    #     sys.exit(
    #         load_entry_point('termtitle==0.1.7', 'console_scripts', 'termtitle')()
    #     )
  end
  test do
    system "#{bin}/termtitle new_title"
  end
end