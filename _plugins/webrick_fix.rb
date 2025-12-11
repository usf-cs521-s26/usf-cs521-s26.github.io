# This is a workaround for this logfile clutter:
#[2025-07-29 14:51:11] ERROR Errno::ECONNRESET: Connection reset by peer @ io_fillbuf - fd:20 
# /Users/phil/.rbenv/versions/3.1.2/lib/ruby/gems/3.1.0/gems/webrick-1.9.1/lib/webrick/httpserver.rb:82:in `eof?'
# /Users/phil/.rbenv/versions/3.1.2/lib/ruby/gems/3.1.0/gems/webrick-1.9.1/lib/webrick/httpserver.rb:82:in `run'
# /Users/phil/.rbenv/versions/3.1.2/lib/ruby/gems/3.1.0/gems/webrick-1.9.1/lib/webrick/server.rb:310:in `block in start_thread'


if Jekyll.env == 'development'
    require 'webrick'

    # Patch WEBrick to handle WebSocket disconnections gracefully
    module WEBrick
        class HTTPServer
        alias_method :original_run, :run

        def run(sock)
            original_run(sock)
        rescue Errno::ECONNRESET, Errno::EPIPE, Errno::ECONNABORTED
            # Client disconnected - this is normal for WebSocket connections
            # Just log it at debug level instead of error
            @logger.debug "Client disconnected: #{$!.class.name}"
        rescue => e
            # Re-raise other errors
            raise e
        end
        end
    end
end
